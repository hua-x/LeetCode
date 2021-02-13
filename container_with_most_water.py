class Solution:
    
    def maxArea(self, height) -> int:
        
        def computeArea(head, tail, height):
            return min(height[head],height[tail]) * abs(tail - head)
    
        length = len(height)
        left = 0
        right = length-1
        area = computeArea(left, right, height)
        print(left, right, area)
        
        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            area = max(computeArea(left, right, height), area)

            print(left, right, area)
            
        return area


if __name__ == '__main__':
    
    sol = Solution()
    height1 = [4,3,2,1,4]
    print(sol.maxArea(height1))
