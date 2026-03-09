class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7

        # dp0[z][o] = number of valid arrays with z zeros and o ones that END with 0
        # dp1[z][o] = number of valid arrays with z zeros and o ones that END with 1
        dp0 = [[0] * (one + 1) for _ in range(zero + 1)]
        dp1 = [[0] * (one + 1) for _ in range(zero + 1)]

        # base: sequences made of only zeros (or only ones) are valid only if length <= limit
        for z in range(1, min(limit, zero) + 1):
            dp0[z][0] = 1
        for o in range(1, min(limit, one) + 1):
            dp1[0][o] = 1

        for z in range(0, zero + 1):
            for o in range(0, one + 1):
                if z == 0 and o == 0:
                    continue

                # compute dp0[z][o] by appending a block of k zeros (1 <= k <= min(limit, z))
                if z > 0:
                    # if o == 0 we've already initialized dp0[z][0]
                    if o > 0:
                        s = 0
                        maxk = min(limit, z)
                        for k in range(1, maxk + 1):
                            s += dp1[z - k][o]
                        dp0[z][o] = s % MOD

                # compute dp1[z][o] by appending a block of k ones (1 <= k <= min(limit, o))
                if o > 0:
                    if z > 0:
                        s = 0
                        maxk = min(limit, o)
                        for k in range(1, maxk + 1):
                            s += dp0[z][o - k]
                        dp1[z][o] = s % MOD
                    # else dp1[0][o] already initialized

        return (dp0[zero][one] + dp1[zero][one]) % MOD