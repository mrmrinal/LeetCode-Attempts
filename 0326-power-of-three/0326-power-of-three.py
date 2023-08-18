class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        curr = n
        while(curr > 1):
            curr = curr / 3
        if curr == 1:
            return True
        else:
            return False
        