library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity spi_slave is
  generic(
    data_length : integer := 576   -- total de bits esperados (72 bytes). 12 sensores, 3 eixos, cada sensor envia 2 bytes
  );
  port(
    reset_n   : in  std_logic;                           -- reset ativo em nível baixo
    cpol      : in  std_logic;                           -- polaridade do clock 
    cpha      : in  std_logic;                           -- fase do clock
    sclk      : in  std_logic;                           -- clock do SPI, determinado pelo master (ESP32)
    ss_n      : in  std_logic;                           -- chip select (ativo em 0)
    mosi      : in  std_logic;                           -- master out, slave in
    miso      : out std_logic;                           -- master in, slave out
    rx_enable : in  std_logic;                           -- habilita saída RX
    tx        : in  std_logic_vector(data_length-1 downto 0);  -- dados a transmitir
    rx        : out std_logic_vector(data_length-1 downto 0);  -- dados recebidos
    busy      : out std_logic;                           -- indica que a transmissão está ocorrendo
    rx_valid  : out std_logic                            -- indica que chegaram todos os bytes
  );
end spi_slave;

architecture Behavioral of spi_slave is

  signal mode       : std_logic;  
  signal clk_int    : std_logic;
  signal bit_index  : integer range 0 to data_length := 0;
  signal rxBuffer   : std_logic_vector(data_length-1 downto 0) := (others => '0');
  signal txBuffer   : std_logic_vector(data_length-1 downto 0) := (others => '0');

begin

  -- busy ativo enquanto CS estiver baixo (recebendo dados)
  busy <= not ss_n;

  -- determina o modo do SPI conforme CPOL/CPHA
  mode <= cpol xor cpha;

  process(mode, ss_n, sclk)
  begin
    if ss_n = '1' then
      clk_int <= '0';
    else
      if mode = '1' then
        clk_int <= sclk;
      else
        clk_int <= not sclk;
      end if;
    end if;
  end process;


  -- Processo de recepção e transmissão SPI
  process(clk_int, ss_n, reset_n)
  begin
    if reset_n = '0' then
      bit_index <= 0;
      rxBuffer  <= (others => '0');
      txBuffer  <= (others => '0');
      miso      <= 'Z';
      rx        <= (others => '0');
      rx_valid <= '0';

    elsif ss_n = '1' then  -- frame terminou / CS inativo
    
      --verificação se todos os bytes chegaram
      if bit_index = data_length then
        rx_valid <= '1';
      end if;
      bit_index <= 0;
      miso <= 'Z';
    
      -- libera dado recebido quando CS sobe 
      if rx_enable = '1' then
        rx <= rxBuffer;
      end if;

      -- recarrega buffer de TX para próxima transação
      txBuffer <= tx;

    else  -- ss_n = '0' => ativo
      rx_valid <= '0';
      if falling_edge(clk_int) then
        -- Shift in: LSB-first
        if bit_index < data_length then
          rxBuffer <= rxBuffer(data_length-2 downto 0) & mosi;
          bit_index <= bit_index + 1;
        end if;
      end if;

      if rising_edge(clk_int) then
        -- Shift out: envia MSB atual
        if bit_index < data_length then
          miso <= txBuffer(data_length-1);
          txBuffer <= txBuffer(data_length-2 downto 0) & txBuffer(data_length-1);
        end if;
      end if;
    end if;
  end process;

end Behavioral;
