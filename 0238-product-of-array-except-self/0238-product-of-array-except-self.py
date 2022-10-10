class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        product = 1
        for num in nums:
            if num == 0:
                zeros += 1
                continue
            product *= num
        res = []
        for num in nums:
            if zeros > 1:
                res.append(0)
            elif zeros == 1:
                if num == 0:
                    res.append(product)
                else:
                    res.append(0)
            else:
                res.append(product//num)
        return res
            
        