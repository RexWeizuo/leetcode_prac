'''将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        '''行数等于1或行数>=字符串长度的情况'''
        if numRows == 1 or numRows >= len(s):
            return s
        
        '''一个空二维字符串列表来存放输出结果'''
        rows = [''] * numRows
        current_row = 0 # 当前字符要存放的row
        going_down = False # 是否向下一行存放

        for char in s:
            rows[current_row] += char
            '''如果是第一行goingdown, 如果是最后一行就不goingdown'''
            if current_row == 0:
                going_down = True
            if current_row == numRows -1:
                going_down = False
            '''current_row根据条件加减'''
            if going_down == True:
                current_row += 1
            else:
                current_row -= 1
        
        return ''.join(rows)

# 测试
s = "PAYPALISHIRING"
numRows = 3
solution = Solution()
print(solution.convert(s, numRows))  # 输出: "PAHNAPLSIIGYIR"