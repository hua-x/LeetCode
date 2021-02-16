class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result = []
        nums = sorted(nums)
        length = len(nums)
        
        for i in range(0, length-3):
            for j in range(i+1, length-2):
                left, right = j + 1, length - 1
                while left < right:
                    if nums[i] + nums[j] + nums[left] + nums[right] > target:
                        right -= 1
                    elif nums[i] + nums[j] + nums[left] + nums[right] < target:
                        left += 1
                    else:
                        if [nums[i], nums[j], nums[left], nums[right]] not in result:
                            result.append([nums[i], nums[j], nums[left], nums[right]])
                        while nums[left] == nums[left+1] and left+1 < right:
                            left += 1 
                        left += 1
                        while nums[right] == nums[right-1] and left < right-1:
                            right -= 1
                        right -= 1
        
        return result
