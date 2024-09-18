'''给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
返回容器可以储存的最大水量。
说明：你不能倾斜容器。'''

'''输入：[1,8,6,2,5,4,8,3,7]
输出：49 
解释：在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49 = 高度7 * 横跨7。

输入：height = [1,1]
输出：1'''

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''左右指针从两边开始看，记录最大面积'''
        l, r = 0, len(height) - 1
        max_area = 0

        while l < r:
            current_area = min(height[l], height[r]) * (r-l)
            max_area = max(max_area, current_area)
        
            '''移动短的指针，寻找可能的更大面积'''
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        
        return max_area
        

# 测试用例
solution = Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7]))  # 输出: 49
print(solution.maxArea([1,1]))                # 输出: 1
