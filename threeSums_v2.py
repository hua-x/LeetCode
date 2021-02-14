import unittest

class Solution:
    def threeSum(self, nums):
        if len(nums) < 3 or min(nums) > 0 or max(nums) < 0:
            return []
        res = []
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        nums = sorted(count)
        for idx, num in enumerate(nums):
            if num > 0:
                break
            two_sum = - num
            num2_min, num2_max = two_sum - nums[-1], two_sum / 2

            i = bisect_left(nums, num2_min, idx + 1)
            j = bisect_left(nums, num2_max, i)
            for num2 in nums[i:j]:
                num3 = two_sum - num2
                if num3 in count:
                    res.append((num, num2, num3))
        for num in nums:
            if count[num] > 1:
                if num == 0 and count[num] >= 3:
                    res.append((num, num, num))
                elif num != 0 and 0 - 2 * num in count:
                    res.append((num, num, 0 - 2 * num))
        return res

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
