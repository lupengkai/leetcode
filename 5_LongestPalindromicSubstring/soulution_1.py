class Solution:
    def longestPalindrome(self, s):
        start, end = 0, 0
        for i in range(len(s)):
            len1 = self.expand_around_center(s, i, i)
            len2 = self.expand_around_center(s, i, i + 1)
            length = max(len1, len2)#两个里面找一个大的
            if length > end-start:
                start = i - (length - 1) // 2
                end = i + length // 2
        return s[start:end+1]

    def expand_around_center(self, s, left, right):  # 对S从给定的位置往两边探索是否对称
        L, R = left, right
        while L >= 0 and R < len(s) and s[L] == s[R]:
            L -= 1
            R += 1

        return R - L - 1 #跳出循环后长度加了2，因此要减掉


