class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = 0
        target = {}
        tracker = {}
        for i in range(len(s1)):
            if s1[i] in target:
                target[s1[i]] += 1
            else:
                target[s1[i]] = 1
        

        while right < len(s2):
            if s2[right] in target:
                if s2[right] in tracker:
                    tracker[s2[right]] += 1
                else:
                    tracker[s2[right]] = 1
                
            while (s2[right] not in target or tracker[s2[right]] > target[s2[right]]) and left < right:
                if s2[left] in tracker and s2[left] in target:
                    tracker[s2[left]] -= 1
                
                left += 1
            
            if tracker == target:
                return True
            
            right += 1
        
        return False
