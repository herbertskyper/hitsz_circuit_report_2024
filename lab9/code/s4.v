module dff_reset_en (
input clk,
input en,
input reset,
input d,
output q);
reg q_reg;
always @( posedge clk , posedge reset )
    begin
        if ( reset ) 
            q_reg <=1'b0;
        else if( en )
            q_reg <= d;
    end

assign q= q_reg;
endmodule