class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        uniqueChar = set()
        maxLen = 0
        while right < len(s):
            if s[right] in uniqueChar:
                uniqueChar.remove(s[left])
                left+=1
            else:
                maxLen = max(maxLen, right - left + 1)
                uniqueChar.add(s[right])
                right += 1

        return maxLen

