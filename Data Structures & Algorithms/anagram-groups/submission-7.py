class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            freq = [0] * 26
            for char in string:
                freq[ord(char) - ord('a')] += 1

            freq = tuple(freq)
            if freq in anagrams:
                anagrams[freq].append(string)
            else:
                anagrams[freq] = [string]
        
        retList = []
        for anagram in anagrams:
            retList.append(anagrams[anagram])
        
        return retList