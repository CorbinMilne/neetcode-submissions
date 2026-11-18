class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {} # key: word in sorted order, value: list of anagrams

        for word in strs:
            key = ''.join(sorted(word))

            if key in d:
                d[key].append(word)
            else:
                d[key] = [word]

        return list(d.values())