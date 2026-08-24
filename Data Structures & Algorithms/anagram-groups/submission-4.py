class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for string in strs:
            letters = [0] * 26
            for i in range(len(string)):
                letters[ord(string[i]) - ord('a')] += 1
            
            anagrams[tuple(letters)].append(string)
            
        
        return list(anagrams.values())