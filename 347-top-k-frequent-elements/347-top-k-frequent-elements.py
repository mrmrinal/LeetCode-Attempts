class Solution:    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        for i in nums:
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1
        res = [key for key, v in sorted(dictionary.items(), key=lambda item: item[1], reverse = True)][:k]
        return res
            
            
            
            
                
        