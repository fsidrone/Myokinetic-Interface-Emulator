library ieee;
use ieee.std_logic_1164.all;

entity spi_module is
    port (
        clk     : in  std_logic;  -- Clock interno da FPGA
        reset   : in  std_logic;  -- Reset síncrono

        -- SPI interface
        sclk    : in  std_logic;  
        mosi    : in  std_logic;  
        miso    : out std_logic;  
        cs      : in  std_logic;
        ready   : out std_logic;
        rx_data : out std_logic_vector(575 downto 0)
    );
end spi_module;

architecture Behavioral of spi_module is

 
    component spi_slave is
        generic (
            data_length : integer := 576
        );
        port (
            reset_n    : in  std_logic;
            cpol       : in  std_logic;
            cpha       : in  std_logic;
            sclk       : in  std_logic;
            ss_n       : in  std_logic;
            mosi       : in  std_logic;
            miso       : out std_logic;
            rx_enable  : in  std_logic;
            tx         : in  std_logic_vector(data_length-1 downto 0);
            rx         : out std_logic_vector(data_length-1 downto 0);
            busy      : out std_logic;                           
            rx_valid  : out std_logic
        );
    end component;
    
    

    -- Sinais internos
    signal reset_n     : std_logic;
    signal cpha  : std_logic := '0';
    signal cpol  : std_logic := '0';
    signal rx_enable   : std_logic := '1';
    signal tx_data     : std_logic_vector(575 downto 0) := (others => '0');
    signal srx_data     : std_logic_vector(575 downto 0);
    signal busy        : std_logic;
    signal busy_d      : std_logic := '0';
    signal sready       : std_logic := '0';
    signal rx_data_out : std_logic_vector(575 downto 0);
    signal busy_sync1, busy_sync2 : std_logic := '0';
    signal capture_en : std_logic := '0';
    signal rx_valid : std_logic := '0';


    
begin

    reset_n <= not reset;
    cpol    <= '0';
    cpha    <= '0';
    rx_enable <= '1';
    ready   <= sready;
    rx_data <= rx_data_out;


    SPI: spi_slave
        generic map (
            data_length => 576
        )
        port map (
            reset_n   => reset_n,
            cpol      => cpol,
            cpha      => cpha,
            sclk      => sclk,
            ss_n      => cs,
            mosi      => mosi,
            miso      => miso,
            rx_enable => rx_enable,
            tx        => tx_data,
            rx        => srx_data,
            busy      => busy,
            rx_valid  => rx_valid
        );
        

    process(clk)
    begin
        if rising_edge(clk) then
            if reset = '1' then
                busy_sync1 <= '0';
                busy_sync2 <= '0';
                busy_d     <= '0';
                sready      <= '0';
                capture_en <= '0';
                rx_data_out <= (others => '0');
    
            else
                -- sincroniza busy do domínio clk SPI para o domínio do clk FPGA
                busy_sync1 <= busy;
                busy_sync2 <= busy_sync1;
                
        
    
                -- detecta borda de descida de busy
                if (busy_d = '1' and busy_sync2 = '0') then
                    capture_en <= '1';      -- ativa captura no próximo ciclo
                    sready      <= '0';
                elsif capture_en = '1' then
                    rx_data_out <= srx_data; 
                    sready <= rx_valid;          
                    capture_en <= '0';
                else
                    sready <= '0';
                end if;
    
                busy_d <= busy_sync2;
            end if;
        end if;
    end process;
    

    

    

end Behavioral;
