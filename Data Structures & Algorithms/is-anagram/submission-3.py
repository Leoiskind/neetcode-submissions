class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        nums = [0] * 26
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            nums[ord(s[i]) - ord('a')] += 1
            nums[ord(t[i]) - ord('a')] -= 1
        
        for i in range(len(nums)):
            if nums[i] != 0:
                return False
        
        return True