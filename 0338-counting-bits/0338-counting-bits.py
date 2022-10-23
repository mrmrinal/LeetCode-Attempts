class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            temp = str(bin(i))
            curr = 0
            for char in temp:
                if char == '1':
                    curr += 1
            res.append(curr)
        return res
        
        