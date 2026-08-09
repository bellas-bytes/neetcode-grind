class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sMapping = {}
        tMapping = {}

        for i, x in enumerate(s):
            if s[i] not in sMapping.keys():
                sMapping[s[i]] = 1
            else:
                sMapping[s[i]] += 1
            
            if t[i] not in tMapping.keys():
                tMapping[t[i]] = 1
            else:
                tMapping[t[i]] += 1
        
        return sMapping == tMapping
