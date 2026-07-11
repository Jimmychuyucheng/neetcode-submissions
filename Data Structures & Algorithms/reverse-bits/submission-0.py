class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res <<= 1 # 相當於res*=2
            res += (n & 1)
            n >>= 1  # 相當於n//=2 
        return res
        

        