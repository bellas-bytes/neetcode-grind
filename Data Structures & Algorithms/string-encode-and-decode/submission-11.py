class Solution:

    def encode(self, strs: List[str]) -> str:
        sentence = ""

        for s in strs:
            str_len = len(s)
            sentence += str(str_len)
            sentence += "#"
            sentence += s
        return sentence

    def decode(self, s: str) -> List[str]:
        print(s)
        i = 0
        decoded = []
        while i < len(s):
            size = ""
            while s[i] != "#":
                size += s[i]
                i += 1
                print(size)
            size_int = int(size)

            i += 1
            decoded.append(s[i: i + size_int])
            i += size_int
        return decoded

