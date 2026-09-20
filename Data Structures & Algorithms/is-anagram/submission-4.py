class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        order = [0] * 26
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            order[ord(s[i]) - ord('a')] += 1
            order[ord(t[i]) - ord('a')] -= 1
        
        if order != [0] * 26:
            return False
        else:
            return True