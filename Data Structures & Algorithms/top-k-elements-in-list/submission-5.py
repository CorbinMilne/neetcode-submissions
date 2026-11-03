from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        d = defaultdict(int) # count : num

        for num in nums:
            d[num] += 1
        
        sorted_items = sorted(d.items(), key=lambda item: item[1], reverse=True)
        sorted_dict = dict(sorted_items)


        for key in sorted_dict.keys():
            if k != 0:
                res.append(key)
                k -= 1

        return res

        