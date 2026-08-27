class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""

        for i in strs:
            enc += str(len(i)) + "#" + i
        
        return enc

    def decode(self, s: str) -> List[str]:

        dec = []
        i = 0

        while i < len(s):

           delp = s.find("#", i)

           length = int(s[i:delp])

           start = delp + 1
           end = start + length

           dec.append(s[start:end])

           i = end

        return dec
