`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2024/07/15 10:29:58
// Design Name: 
// Module Name: ex3
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


module dff_reset (
input clk,
input reset,
input d,
output q);
reg q_reg;
always @( posedge clk , posedge reset )
    begin
        if ( reset ) 
            q_reg <=1'b0;
        else
            q_reg <= d;
    end

assign q= q_reg;
endmodule
