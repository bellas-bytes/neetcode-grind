class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            word_mapping = {}
            for letter in word:
                if letter not in word_mapping:
                    word_mapping[letter] = 1
                else:
                    word_mapping[letter] += 1
            items = tuple(sorted(word_mapping.items()))
            if items not in anagrams.keys():
                anagrams[items] = [word]
            else:
                anagrams[items].append(word)
        return [x for x in anagrams.values()]
