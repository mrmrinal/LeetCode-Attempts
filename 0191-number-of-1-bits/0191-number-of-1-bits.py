class Solution:
    def hammingWeight(self, n: int) -> int:
        list_n = bin(n)
        count = 0
        for i in range(0, len(list_n)):
            if list_n[i] == '1':
                count += 1
        return count
        