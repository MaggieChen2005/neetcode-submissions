class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        # encode to be like [5#Hello6#World!]
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        index = 0
        
        while index < len(s):
            j = index # j finds the index where # is 
            while s[j] != "#":
                j += 1
            length = int(s[index:j])
            result.append(s[j + 1: j + 1 + length]) 
            # j is at # so j + 1 is at the first char of the next work

            index = j + 1 + length
        return result