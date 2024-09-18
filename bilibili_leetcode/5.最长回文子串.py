'''给你一个字符串 s，找到 s 中最长的回文子串。

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。

输入：s = "cbbd"
输出："bb"'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''长度为1的字符串直接返回'''
        if len(s) < 2:
            return s
        '''dp[i][j] 记录子串 i..j 是否为回文串'''
        dp = [[False] * len(s) for _ in range(len(s))] # np.zeros((s,s))
        '''对角线上的元素都为True,长度为1的子串都是回文串'''
        for i in range(s):
            dp[i][i] = True
        start = 0
        max_l = 0

        '''处理长度为2的子串'''
        for i in range(len(s)):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                start = i
                max_l = 2
        
        '''处理长度大于2的子串'''
        for length in range(3, len(s)):
            for i in range(len(s)-length):
                j = i - length - 1
                if s[i] == s[j] and dp[i+1][j-1] == True:
                    dp[i][j] = True
                    start = i
                    max_l = length
        
        return s[start:start+max_l]


s = "ccc"
s1 = Solution()
print(s1.longestPalindrome(s))



