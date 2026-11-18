class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        # nums: [2, 1, 3, 4]
        for num in nums_set:
            # check if previous number is in set to know if we need to start a new length
            if num - 1 not in nums_set:
                length = 1
                current = num

                # iterate until no more consecutive numbers
                while current + 1 in nums_set:
                    length += 1
                    current += 1

                longest = max(longest, length)

        return longest




        
        