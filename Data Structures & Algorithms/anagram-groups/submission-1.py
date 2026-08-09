class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort_str = {}
        for i, s in enumerate(strs):
            temp = sorted(s)
            temp_str = "".join(temp)

            if temp_str not in sort_str.keys():
                sort_str[temp_str] = [s]
            else:
                sort_str[temp_str].append(s)
        
        return list(sort_str.values())