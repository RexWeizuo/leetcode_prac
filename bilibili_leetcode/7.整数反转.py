'''给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。
假设环境不允许存储 64 位整数（有符号或无符号）。

示例 1：
输入：x = 123
输出：321

示例 2：
输入：x = -123
输出：-321

示例 3：
输入：x = 120
输出：21

示例 4：
输入：x = 0
输出：0'''

class Solution:
    def reverse(self, x: int) -> int:
        # 定义32位整数范围
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        '''x先取绝对值，最后返回的时候乘上正负号'''
        sign = 1 if x >= 0 else -1
        x = abs(x)

        reversed_num = 0
        '''处理x不等于0的情况，如果x=0，直接返回初始化为0的reversed_num'''
        while x != 0:
            pop = x % 10 # 取末位
            x //= 10 # 去末位

            # 检查是否溢出
            if (reversed_num > INT_MAX // 10) or (reversed_num == INT_MAX // 10 and pop > 7):
                return 0
            if (reversed_num < INT_MIN // 10) or (reversed_num == INT_MIN // 10 and pop > 8):
                return 0


            '''末位*10+上一位数，完成反转'''
            reversed_num = reversed_num * 10 + pop
        
        return reversed_num * sign



# 测试用例
solution = Solution()
print(solution.reverse(123))    # 输出: 321
print(solution.reverse(-123))   # 输出: -321
print(solution.reverse(120))    # 输出: 21
print(solution.reverse(0))      # 输出: 0