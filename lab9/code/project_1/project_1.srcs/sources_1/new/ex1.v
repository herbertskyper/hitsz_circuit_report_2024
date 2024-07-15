`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2024/07/15 10:12:36
// Design Name: 
// Module Name: ex1
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module Vr2to4dec_s(
input EN,
input in_A0,
input in_A1,
output out_Y0,
output out_Y1,
output out_Y2,
output out_Y3
);
    wire not_A0, not_A1;
    
    not U1(not_A0, in_A0); 
    not U2(not_A1, in_A1); 
    and U3(out_Y0, EN, not_A1, not_A0);
    and U4(out_Y1, EN, not_A1, in_A0);
    and U5(out_Y2, EN, in_A1, not_A0);
    and U6(out_Y3, EN, in_A1, in_A0);

endmodule
