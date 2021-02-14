import unittest

class Solution:
    
    def twoSum(self, nums, ans):
        result = []
        dic = {}
        for i in range(len(nums)):
            item = nums[i]
            key = str(item)
            if key not in dic:
                dic[key] = ans-item
            if dic[key] in nums[i+1:] and [item, dic[key]] not in result:
                result.append([item,dic[key]])        
        return result

    def threeSum(self, nums):
        sorted_nums = sorted(nums)
        dic = {}
        result = []
        for i in range(len(sorted_nums)):
            item = sorted_nums[i]
            if item in dic:
                continue
            results = self.twoSum(sorted_nums[i+1:],-item)
            if results:
                for res in results:
                    if [item] + res not in result:
                        result.append([item] + res)
                        dic[item] = results

        return result

class TestCases(unittest.TestCase):
    sol = Solution()

    def test_base(self):
        nums = [-1,0,1,2,-1,-4]
        self.assertEqual(self.sol.threeSum(nums),[[-1,-1,2], [-1,0,1]])

    def test_null(self):
        nums = []
        self.assertEqual(self.sol.threeSum(nums),[])

    def test_oneZero(self):
        nums = [0]
        self.assertEqual(self.sol.threeSum(nums),[])

if __name__ == '__main__':
    unittest.main()
