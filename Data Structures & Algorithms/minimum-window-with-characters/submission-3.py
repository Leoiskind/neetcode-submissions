class Solution:
    def minWindow(self, s: str, t: str) -> str:
        substringlen = float('inf')
        right = 0
        left = 0
        tally = 0
        tFreq = {}
        for char in t:
            if char in tFreq:
                tFreq[char] += 1
            else:
                tFreq[char] = 1
        
        sFreq = {}

        while right < len(s):
            if s[right] in tFreq:
                if s[right] in sFreq:
                    sFreq[s[right]] += 1
                else:
                    sFreq[s[right]] = 1
                
                if sFreq[s[right]] == tFreq[s[right]]:
                    tally += 1

            while tally == len(tFreq.keys()):
                if s[left] in tFreq:
                    sFreq[s[left]] -= 1
                    if sFreq[s[left]] < tFreq[s[left]]:
                        tally -= 1
                        
                        if(right - left + 1) < substringlen:
                            bounds = [left, right+1]
                            substringlen = right - left + 1
                left += 1

            right += 1
        
        if substringlen <= len(s):
            return s[bounds[0]: bounds[1]]
        return ""