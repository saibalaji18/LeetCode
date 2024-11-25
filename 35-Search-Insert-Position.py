class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        k = 0
        if target in nums:
            k = nums.index(target)

        elif target not in nums and len(nums) == 1:
            if target > nums[0]:
                k = len(nums)

        elif target not in nums and len(nums) > 1:
            for i in range (len(nums)-1):
                if target > nums [i-1] and target < nums[i]:
                    k = i
                elif target > nums[i] and target < nums[i+1]:
                    k = i+1
                elif target > nums[len(nums)-1]:
                    k = len(nums)

        return k 

        