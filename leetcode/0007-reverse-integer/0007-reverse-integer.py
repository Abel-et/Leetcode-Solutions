class Solution:
    def reverse(self, x: int) -> int:
        # declare  lower and upper bond 
        lower = -2**31
        upper = 2**31 - 1

        # assing a sign of x
        sign = 1 if x >= 0 else -1

        # convert int to str to make reverse
        res_st = str(abs(x))[::-1]
        res_int = int(res_st) * sign

        # check the reveresed  integer  is greater or lower to bondes
        if res_int < lower or res_int > upper:
            return 0
        return res_int