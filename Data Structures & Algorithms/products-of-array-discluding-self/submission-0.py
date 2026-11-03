class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        ans = []
        idx = 0

        for num in nums:
            if idx == len(nums) - 1:
                prod = nums[0]
            else:
                prod = nums[idx + 1]

            idx_2 = 0
            for i in nums:
                if idx_2 != idx and idx_2 != (idx + 1) % len(nums):
                    prod *= i
                idx_2 += 1

            ans.append(prod)
            idx += 1

        return ans
