class Solution:
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        ans = 0
        window = {}
        i, j = 0, 0
        while j < n:
            if s[j] in window.keys():#历史窗和当前窗
                i = max(window[s[j]], i) #判断是不是当前窗内的字符
            ans = max(ans, j-i+1)
            window[s[j]] = j+1#更新该字符的位置并设为下一个起始位置
            j += 1
        print(ans)
        return ans

Solution().lengthOfLongestSubstring('abcabcbb')
Solution().lengthOfLongestSubstring('bbbbb')
Solution().lengthOfLongestSubstring('pwwkew')
# Solution().lengthOfLongestSubstring('')
# Solution().lengthOfLongestSubstring('c')
# Solution().lengthOfLongestSubstring('ca')