class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}

        for word in strs:
            sortedWord = "".join(sorted(word))

            if sortedWord not in words:
                words[sortedWord] = [word]
            else:
                words[sortedWord].append(word)
  
        return list(words.values())