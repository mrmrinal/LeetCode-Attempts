class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            curr = 0
            for char in bin(i):
                if char == '1':
                    curr += 1
            res.append(curr)
        return res
        
        