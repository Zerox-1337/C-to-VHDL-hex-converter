# C-to-VHDL-hex-converter

When getting hex values from a C code they sometimes don't match the output from a VHDL testbench, the reason being that the C reads the bytes from opposite order. This code takes a hex value, divide it up into bytes, reverse the bit order and then prints new hex value. It also contains a bonus feature which is to print out the hex values in a VHDL testbench format using "after"
