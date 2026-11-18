class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # output[i] = left_product * right_product
        output = [1] * len(nums)

        # nums   = [2, 3, 4, 5]
        # output = [1, 2, 6, 24]
        left_product = 1
        for i in range(len(nums)):
            output[i] = left_product
            left_product *= nums[i]

        # output = [60, 40, 30, 24]
        right_product = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]

        return output

        




        



            



