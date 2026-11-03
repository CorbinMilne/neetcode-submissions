class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                nums.pop(i)
            else:
                cnt += 1
        
        return cnt