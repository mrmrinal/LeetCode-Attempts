class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while(left < len(s) and left < right):
            if right == left:
                return True
            while(not s[left].isalnum()):
                left += 1
                if left >= len(s) or right < 0:
                    return True
            while(not s[right].isalnum()):
                right -= 1
                if left >= len(s) or right < 0:
                    return True
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True
            
        