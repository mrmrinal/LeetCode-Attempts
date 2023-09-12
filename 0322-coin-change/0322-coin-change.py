class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        res = [float('inf')] * (amount + 1)
        res[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    res[i] = min(res[i], res[i - coin] + 1)
        
        return res[amount] if res[amount] != float('inf') else -1