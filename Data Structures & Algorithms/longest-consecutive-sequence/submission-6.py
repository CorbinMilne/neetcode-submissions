class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        counts = []
        count = 1

        sorted_nums = sorted(nums)

        for i in range(1, len(sorted_nums)):

            if sorted_nums[i] - sorted_nums[i-1] == 1:
                count += 1
            elif sorted_nums[i] == sorted_nums[i - 1]:
                continue
            else:
                counts.append(count)
                count = 1

        counts.append(count)

        if counts:
            return max(counts)
        
        else:
            return count
        
        