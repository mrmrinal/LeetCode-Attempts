class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for string in strs:
            ordered = sorted(string)
            ordered = "".join(ordered)
            if ordered in dictionary:
                dictionary[ordered].append(string)
            else:
                dictionary[ordered] = [string]
        res = []
        for v in dictionary.values():
            res.append(v)
        return res
        