'''给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。'''

def lengthOfLongestSubstring(s: str) -> int:
    # 使用字典来存储字符最近出现的位置
    char_index = {}
    max_length = 0
    start = 0
 
    for i, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            # 更新起始位置为重复字符的下一个位置
            start = char_index[char] + 1
        else:
            # 更新最大长度
            max_length = max(max_length, i - start + 1)
 
        # 更新字符最近出现的位置
        char_index[char] = i
 
    return max_length
 
# 测试
s = "abcabcbb"
print(lengthOfLongestSubstring(s))  # 输出 3，对应的最长子串为 "abc"
 
s = "bbbbb"
print(lengthOfLongestSubstring(s))  # 输出 1，对应的最长子串为 "b"
 
s = "pwwkew"
print(lengthOfLongestSubstring(s))  # 输出 3，对应的最长子串为 "wke"