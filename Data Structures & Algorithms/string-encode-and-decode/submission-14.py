class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        fstring=""
        for string in strs:
            length = len(string)
            fstring += str(length) + "#" + string
        
        return fstring

    def decode(self, s: str) -> List[str]:
        strings = []
        if not s:
            return strings
        i = 0
        while i < len(s):
            num = ""
            for j in range(i, len(s)):
                if(s[j]=='#'):
                    i = j+1
                    break
                num += s[j]
            
            strings.append(s[i:i+int(num)])
            i = i + int(num)
        return strings