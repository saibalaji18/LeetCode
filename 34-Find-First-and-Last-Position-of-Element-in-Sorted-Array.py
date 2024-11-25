class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a = []
        if target not in nums:
            return [-1,-1]

        elif target in nums and len(nums) == 1:
            a.append(nums.index(target))
            a.append(nums.index(target))

        elif target in nums and len(nums) > 1 and nums.count(target) == 1:
            a.append(nums.index(target))
            a.append(nums.index(target))
        
        elif target in nums and nums.count(target) > 2:   
            s = 0
            a.append(nums.index(target))
            for i in range (len(nums)):
                if target == nums[i]:
                    s = i
            a.append(s)
                
        else:
            for i in range (len(nums)):
                if target == nums[i]:
                    a.append(i)
        return a
        
