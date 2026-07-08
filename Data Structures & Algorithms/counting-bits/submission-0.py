class Solution:
    def countBits(self, n: int) -> List[int]:
        # 0-1 cycle = 1, 2, 4, 8
        '''
        start from 0
        0th: 2n-1
        1st: 4n-2, 4n-1 34781112
        2nd: 

        '''
        res = []
        for num in range(n+1):
            res.append(bin(num).count("1"))

        return res

        