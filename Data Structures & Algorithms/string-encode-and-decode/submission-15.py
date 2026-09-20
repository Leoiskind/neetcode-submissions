class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string)) + '#' + string
        return encoded
    def decode(self, s: str) -> List[str]:
        decoded = []
        pointer = 0
        while pointer < len(s):
            string = ""
            num = ""
            while pointer < len(s) and s[pointer] != '#':
                num += s[pointer]
                pointer += 1
            
            for i in range(int(num)):
                pointer += 1
                string += s[pointer]
            
            decoded.append(string)
            pointer += 1
        
        return decoded