class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums = sorted(nums)
        length = len(nums)
        start = end = length-1
          
        while True:
            while nums[start] == nums[end] and end >= 0:
                end = end - 1
            print(start, end)
            if start - end > 1:
                print(nums[end+1: start])
                del nums[end+1: start]
                print(nums)
            
            if end < 0:
                break
            else:
                start = end
            
        #print(start, end)
        #print(len(nums))
        return len(nums)
