class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currMax = 0
        minSum = nums [0]
        currMin = 0
        total = 0

        for n in nums:
            currMax = max(currMax, 0)
            currMin = min(currMin, 0)
            currMax += n
            currMin += n
            total += n
            maxSum = max(maxSum, currMax)
            minSum = min(minSum, currMin)

        return max(maxSum, total - minSum) if maxSum > 0 else maxSum