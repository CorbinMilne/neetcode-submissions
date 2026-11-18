class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {} #key: num, value: count of num
        res = []
        count = 0

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        #descending order
        sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))

        for key in sorted_freq:
            if count != k:
                res.append(key)
                count += 1
            else:
                break
            

        return res
