----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 06.11.2025 16:01:44
-- Design Name: 
-- Module Name: topmodule - Behavioral
-- Project Name: 
-- Target Devices: 
-- Tool Versions: 
-- Description: 
-- 
-- Dependencies: 
-- 
-- Revision:
-- Revision 0.01 - File Created
-- Additional Comments:
-- 
----------------------------------------------------------------------------------


library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity topmodule is
    generic(
        num_spi : integer := 4   -- total de bits esperados (72 bytes). 12 sensores, 3 eixos, cada sensor envia 2 bytes
     );
    Port ( clk   : in STD_LOGIC;
           reset : in STD_LOGIC;
           sclk: in std_logic_vector(0 to num_spi-1);
           mosi: in std_logic_vector(0 to num_spi-1);
           miso: out std_logic_vector(0 to num_spi-1);
           cs: in std_logic_vector(0 to num_spi-1));
end topmodule;

architecture Behavioral of topmodule is

component spi_module is
    port (
        clk     : in  std_logic;  
        reset   : in  std_logic;  
        sclk    : in  std_logic;  
        mosi    : in  std_logic;  
        miso    : out std_logic;  
        cs      : in  std_logic;
        ready   : out std_logic;
        rx_data : out std_logic_vector(575 downto 0)
    );
end component;

COMPONENT ila_0
PORT (
	clk : IN STD_LOGIC;
	probe0 : IN STD_LOGIC_VECTOR(0 DOWNTO 0);
	probe1 : IN STD_LOGIC_VECTOR(2303 DOWNTO 0)
);
END COMPONENT  ;

type rx_array is array (0 to num_spi-1) of std_logic_vector(575 downto 0);

-- Sinais dos módulos SPI --
signal ready_spi: std_logic_vector(0 to num_spi-1);
signal rx_spi : rx_array := (others => (others => '0'));

-- Dados coletados ---
signal ready,s_ready, ff_rdy1, ff_rdy2, ff_rdy3, ff_rdy4: std_logic := '0'; 
signal data_spi1, data_spi2, data_spi3 ,data_spi4: std_logic_vector(575 downto 0);
signal frame: std_logic_vector(2303 downto 0);

begin


spi_modules: for i in 0 to num_spi-1 generate
    SPI: spi_module
    port map (
        clk     => clk,
        reset   => reset,
        sclk    => sclk(i),
        mosi    => mosi(i),  
        miso    => miso(i), 
        cs      => cs(i),
        ready   => ready_spi(i),
        rx_data => rx_spi(i)
    );
end generate;

    ila : ila_0
    PORT MAP (
        clk => clk,
        probe0(0) => ready,
        probe1 => frame
    );

process(clk,reset)
    begin
        if rising_edge(clk) then
            if reset='1' or s_ready='1' then
                frame <= (others => '0');
                ff_rdy1 <= '0';
                ff_rdy2 <= '0';
                ff_rdy3 <= '0';
                ff_rdy4 <= '0';
                data_spi1 <= (others => '0');
                data_spi2 <= (others => '0');
                data_spi3 <= (others => '0');
                data_spi4 <= (others => '0');
            else
                if ready_spi(0)='1' then
                    ff_rdy1 <= '1';
                    data_spi1 <= rx_spi(0);
                end if;
                if ready_spi(1)='1' then
                    ff_rdy2 <= '1';
                    data_spi2 <= rx_spi(1);
                end if;
                if ready_spi(2)='1' then
                    ff_rdy3 <= '1';
                    data_spi3 <= rx_spi(2);
                end if;
                if ready_spi(3)='1' then
                    ff_rdy4 <= '1';
                    data_spi4 <= rx_spi(3);
                end if;
            end if;
        end if;
    end process;

s_ready <= ff_rdy1 and ff_rdy2 and ff_rdy3 and ff_rdy4;
ready <= s_ready;
frame <= data_spi1 & data_spi2 & data_spi3 & data_spi4;

end Behavioral;
