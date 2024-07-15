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