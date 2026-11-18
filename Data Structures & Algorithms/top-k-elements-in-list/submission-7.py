from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = {} #key: num, value: frequency of num
        count = k

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))

        for key in sorted_freq:
            if count:
                res.append(key)
            else:
                break
            count -= 1

        return res



        