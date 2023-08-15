memo = [-1] * 10000
memo[0] = 0
memo[1] = 1
memo[2] = 2
class Solution:
    
    def climbStairs(self, n: int) -> int:
        if memo[n] != -1:
            return memo[n]
        else:
            memo[n] = self.climbStairs(n - 1) + self.climbStairs(n -2)
            return memo[n]
        
        