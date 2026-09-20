class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        retList = []
        for string in strs:
            freq = {}
            tup = []
            for char in string:
                if char in freq:
                    freq[char] += 1
                else:
                    freq[char] = 1
            
            for char in freq:
                tup.append((char, freq[char]))

            tup.sort()
            tup = tuple(tup)
            
            if tup in anagrams:
                anagrams[tup].append(string)
            else:
                anagrams[tup] = [string]
        
        for i in anagrams:
            retList.append(anagrams[i])
        
        return retList