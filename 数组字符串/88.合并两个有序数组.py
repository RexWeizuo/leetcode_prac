'''给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，
另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。'''

'''输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
解释：需要合并 [1,2,3] 和 [2,5,6] 。
合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。'''

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # # 直接把num2放到nums1后面然后sort
        # for i in range(n):
        #     nums1[m+i] = nums2[i]
        # nums1.sort()
        
        # 从后往前按元素比较,大的放到新数组末尾
        # 怎么从后往前拿出数组元素呢？指针+while
        p1, p2, p = m-1, n-1, m+n-1
        while p2 >= 0:
            # 怎么比较呢
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

# nums1 = [1,2,3,0,0,0] 
nums1 = [0]
m = 0 
nums2 = [1]
n = 1
s = Solution()
s.merge(nums1, m, nums2, n)
            
        

        
        