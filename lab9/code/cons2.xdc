set_property PACKAGE_PIN M4 [get_ports in_A];
set_property PACKAGE_PIN N4 [get_ports in_B];
set_property PACKAGE_PIN R1 [get_ports in_C];
set_property PACKAGE_PIN K2 [get_ports out_Y];

set_property IOSTANDARD LVCMOS33 [get_ports in_A];
set_property IOSTANDARD LVCMOS33 [get_ports in_B];
set_property IOSTANDARD LVCMOS33 [get_ports in_C];
set_property IOSTANDARD LVCMOS33 [get_ports out_Y];

set_property BITSTREAM.CONFIG.UNUSEDPIN PULLNONE [current_design];