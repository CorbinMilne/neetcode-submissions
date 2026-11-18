class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {} #key: sorted word value: list of anagrams

        for word in strs:
            key = ''.join(sorted(word)) #sorted('cat') - ['a', 'c', 't']

            if key not in groups:
                groups[key] = [word]
            else:
                groups[key].append(word)

        return list(groups.values())
        