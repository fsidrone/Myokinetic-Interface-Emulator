# Artix7 xdc
# define clock and period
create_clock -period 10.000 -name clk -waveform {0.000 5.000} [get_ports clk]
create_clock -name sclk_1 -period 1000.0 [get_ports sclk[0]]  ;# 1 MHz
create_clock -name sclk_2 -period 1000.0 [get_ports sclk[1]]  ;# 1 MHz
create_clock -name sclk_3 -period 1000.0 [get_ports sclk[2]]  ;# 1 MHz
create_clock -name sclk_4 -period 1000.0 [get_ports sclk[3]]  ;# 1 MHz





## Create a virtual clock for IO constraints
create_clock -period 10.000 -name virtual_clock

## input delay
set_input_delay -clock clk -max 2.0 [get_ports reset]
set_input_delay -clock clk -min 1.0 [get_ports reset]

set_input_delay -clock sclk_1 -max 2.0 [get_ports {mosi[0] cs[0]}]
set_output_delay -clock sclk_1 -max 1.0 [get_ports miso[0]]

set_input_delay -clock sclk_2 -max 2.0 [get_ports {mosi[1] cs[1]}]
set_output_delay -clock sclk_2 -max 1.0 [get_ports miso[1]]
set_property CLOCK_DEDICATED_ROUTE FALSE [get_nets {cs_IBUF[1]}]


set_input_delay -clock sclk_3 -max 2.0 [get_ports {mosi[2] cs[2]}]
set_output_delay -clock sclk_3 -max 1.0 [get_ports miso[2]]
set_property CLOCK_DEDICATED_ROUTE FALSE [get_nets {cs_IBUF[2]}]


set_input_delay -clock sclk_4 -max 2.0 [get_ports {mosi[3] cs[3]}]
set_output_delay -clock sclk_4 -max 1.0 [get_ports miso[3]]
set_property CLOCK_DEDICATED_ROUTE FALSE [get_nets {cs_IBUF[3]}]



#set_input_delay -clock clk -max 2.0 [get_ports {sclk}]
#set_input_delay -clock clk -min 1.0 [get_ports {sclk}]
#set_input_delay -clock clk -max 2.0 [get_ports {sclk[1]}]
#set_input_delay -clock clk -min 1.0 [get_ports {sclk[1]}]
#set_input_delay -clock clk -max 2.0 [get_ports {sclk[2]}]
#set_input_delay -clock clk -min 1.0 [get_ports {sclk[2]}]

#set_input_delay -clock clk -max 2.0 [get_ports {mosi}]
#set_input_delay -clock clk -min 1.0 [get_ports {mosi}]
#set_input_delay -clock clk -max 2.0 [get_ports {mosi[1]}]
#set_input_delay -clock clk -min 1.0 [get_ports {mosi[1]}]
#set_input_delay -clock clk -max 2.0 [get_ports {mosi[2]}]
#set_input_delay -clock clk -min 1.0 [get_ports {mosi[2]}]

#set_input_delay -clock clk -max 2.0 [get_ports {cs}]
#set_input_delay -clock clk -min 1.0 [get_ports {cs}]
#set_input_delay -clock clk -max 2.0 [get_ports {cs[1]}]
#set_input_delay -clock clk -min 1.0 [get_ports {cs[1]}]
#set_input_delay -clock clk -max 2.0 [get_ports {cs[2]}]
#set_input_delay -clock clk -min 1.0 [get_ports {cs[2]}]


#set_input_delay -clock clk -max 2.0 [get_ports reset]
#set_input_delay -clock clk -min 1.0 [get_ports reset]
##set_input_delay -clock virtual_clock -max 2.0 [get_ports start]
##set_input_delay -clock virtual_clock -min 1.0 [get_ports start]



##output delay
#set_output_delay -clock virtual_clock 0.2 [get_ports {ready[0]}]
#set_output_delay -clock virtual_clock 0.2 [get_ports {ready[1]}]
#set_output_delay -clock virtual_clock 0.2 [get_ports {ready[2]}]

