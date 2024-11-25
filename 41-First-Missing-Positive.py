class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        k = 0
        nums.sort()
        nums = list(set(nums))
        nums.sort()
        print(nums)
        if nums[0] > 1:
            k = 1
        elif nums[0] < 0 and nums.count(1) > 0:
            for i in range (len(nums)-1):
                if nums[i] < 0 and nums[len(nums)-1] == 1:
                    k = 2
                    break
                if nums[i] <= 0:
                    continue
                if nums[i] >= 1 and nums[i+1] != nums[i]+1:
                    k = nums[i] + 1
                    break
                if nums[i] >= 1 and nums[i+1] == nums[i]+1:
                    k = nums[len(nums)-1] + 1
                
                
        elif len(nums) == 1 and nums[0] >= 0:
            k = nums[0]+1
        elif len(nums) == 1 and nums[0] < 0:
            k = 1
        else:
            for i in range (len(nums)-1):
                if nums[i+1] != nums[i]+1:
                    k = nums[i]+1
                    if k != 0:
                        break
                if nums[0] == 0 and nums[i]+1 == nums[i+1]:
                    k = nums[len(nums)-1]+1
                if nums[0] == 1 and nums[i]+1 == nums[i+1]:
                    k = nums[len(nums)-1]+1

        if k > 0:        
            return k
        else:
            k = 1
            return k