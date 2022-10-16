class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        chars = []
        chars[:0] = palindrome
        print(chars)
        if len(chars) % 2 == 1:
            mid = len(chars) // 2
            for i in range(len(chars)):
                if i == mid:
                    continue
                else:
                    if chars[i] == 'a':
                        continue
                    else:
                        chars[i] = 'a'
                        return "".join(chars)
        else:
            for i in range(len(chars)):
                if chars[i] == 'a':
                    continue
                else:
                    chars[i] = 'a'
                    return "".join(chars)
        for i in range(len(chars)):
            if len(chars) % 2 == 1 and i == len(chars) // 2:
                continue
            if chars[i] != 'a':
                return ""
        chars[-1] = 'b'
        return ''.join(chars)
            
                    
        