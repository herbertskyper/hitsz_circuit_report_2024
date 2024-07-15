module Refree_s(
input in_A,
input in_B,
input in_C,
output out_Y
);
    wire or_A0;
    
    or U1(or_A0, in_B, in_C);
    and U2(out_Y, in_A, or_A0);

endmodule