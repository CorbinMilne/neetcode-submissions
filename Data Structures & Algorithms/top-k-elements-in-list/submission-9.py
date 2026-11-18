class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {} #key: number, value: count of that number
        res = []
        count = 0

        # build dict
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1

        sorted_d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

        for key in sorted_d:
            if count != k:
                res.append(key)
                count += 1
            else:
                break

        return res
        