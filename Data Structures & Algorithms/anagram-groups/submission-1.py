class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(list)

        for word in strs:
            x = "".join(sorted(word))
            words[x].append(word)

        return list(words.values())