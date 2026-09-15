class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        longest = 0
        maxfreq = 0
        freq = {}
        while right < len(s):
            if s[right] in freq:
                freq[s[right]] += 1
            else:
                freq[s[right]] = 1
            
            maxfreq = max(freq.values())
            
            while (right - left+1) - maxfreq > k:
                freq[s[left]] -= 1
                left+= 1
                maxfreq = max(freq.values())
            
            if longest < (right - left+1):
                longest = right-left+1

            right+=1

        return longest