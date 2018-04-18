#暴力求解，超时。验证所有的子串
class Solution:
    def longestPalindrome(self, s):
        ans_string = ''
        for i in range(len(s)):
            for j in range(i, len(s)):
                curr_string = self.find_bound(s[i:j + 1])
                if len(curr_string) >= len(ans_string):
                    ans_string = curr_string
        return ans_string

    def find_bound(self, s):
        sub_string = ''

        if len(s) % 2 == 0:  # 偶数个
            j = len(s) // 2
            i = j - 1
        else:  # 奇数个
            i = len(s) // 2 - 1
            j = i + 2
            sub_string=s[i+1]
        while i >= 0:
            if s[i] == s[j]:
                sub_string = s[i:j + 1]
                i -= 1
                j += 1
            else:
                break
        return sub_string

    """
    :type s: str
    :rtype: str
    """
print(Solution().longestPalindrome('babad'))
print(Solution().longestPalindrome('cbbd'))
print(Solution().longestPalindrome('a'))

