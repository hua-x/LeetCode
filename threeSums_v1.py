import unittest

class Solution:
    
    def threeSum(self, nums):
        sorted_nums = sorted(nums)
        result = []
        
        for i, item in enumerate(sorted_nums):
            if item == sorted_nums[i-1] and i > 0:
                continue

            left, right = i+1, len(sorted_nums)-1
            while left < right:
                total = item + sorted_nums[left] + sorted_nums[right]
                if total > 0:
                    right = right-1
                elif total < 0:
                    left = left+1
                else:
                    result.append([item, sorted_sums[left], sorted_sums[right]])
                    left = left +1
                    while sorted_nums[left] == sorted_nums[left-1] and left < right:
                        left = left + 1

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
