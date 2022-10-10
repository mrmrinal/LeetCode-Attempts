class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        contains = set()
        for val in nums:
            if val not in contains:
                contains.add(val)
            else:
                return True
        return False
        