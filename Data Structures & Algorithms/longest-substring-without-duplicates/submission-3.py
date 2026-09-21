class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        maxLen = 0
        letters = set()

        while right < len(s):
            while s[right] in letters:
                length = right - left
                if length > maxLen:
                    maxLen = length
                letters.remove(s[left])
                left += 1
            letters.add(s[right])
            right += 1
        
        length = right - left
        if length > maxLen:
            maxLen = length
        return maxLen


