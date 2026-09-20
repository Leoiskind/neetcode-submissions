class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        s = s.lower()

        while right > left:
            while right > left and not s[right].isalnum():
                right -= 1
            
            while right > left and not s[left].isalnum():
                left += 1
            
            if right > left and s[right] != s[left]:
                return False
            
            left += 1
            right -= 1
        
        return True