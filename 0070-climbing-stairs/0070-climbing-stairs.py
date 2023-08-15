class Solution:
    
    def climbStairs(self, n: int) -> int:
        curr, next = 0, 1
        iter = 0
        while(iter != n):
            curr, next = next, curr + next
            iter += 1
        return next
        
        