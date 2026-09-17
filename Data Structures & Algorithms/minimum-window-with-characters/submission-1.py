class Solution:
    def minWindow(self, s: str, t: str) -> str:
        substring = s
        right = 0
        left = 0
        tally = 0
        valid = False
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
            
            if tally == len(tFreq.keys()):
                valid = True
                
            while tally == len(tFreq.keys()):
                if s[left] in tFreq:
                    sFreq[s[left]] -= 1
                    if sFreq[s[left]] < tFreq[s[left]]:
                        tally -= 1
                        
                        if(right - left + 1) < len(substring):
                            substring = s[left:right+1]
                left += 1

            right += 1
        
        if valid:
            return substring
        return ""