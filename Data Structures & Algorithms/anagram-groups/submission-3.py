class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            letters = [0] * 26
            for i in range(len(string)):
                letters[ord(string[i]) - ord('a')] += 1
            
            temp = tuple(letters)
            if(temp in anagrams):
                anagrams[temp].append(string)
            else:
                anagrams[temp] = [string]
        
        return list(anagrams.values())