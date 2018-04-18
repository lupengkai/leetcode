class Solution:
    def lengthOfLongestSubstring(self, s):
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1

        longest_substring=""


        next_start_inx= 0


        while True:
            curr_start_inx = next_start_inx
            #print('csi:'+str(curr_start_inx))
            curr_substring = ''
            curr_substring_dict={}
            for i in range(curr_start_inx,len(s)):

                # 从curr_start_inx开始找不重复的串

                if s[i] in curr_substring_dict.keys():
                    if len(curr_substring) > len(longest_substring):
                        longest_substring = curr_substring
                    if len(longest_substring) > len(s)-curr_start_inx-1-curr_substring_dict[s[i]]:
                        print('cut'+longest_substring)
                        return len(longest_substring)
                    next_start_inx = curr_start_inx+curr_substring_dict[s[i]]+1
                    break
                else:
                    curr_substring += s[i]
                    curr_substring_dict[s[i]]=len(curr_substring)-1
                    if i == len(s) -1:
                        if len(curr_substring) > len(longest_substring):
                            longest_substring = curr_substring
                        print(longest_substring)
                        return len(longest_substring)
                    continue



Solution().lengthOfLongestSubstring('abcabcbb')
Solution().lengthOfLongestSubstring('bbbbb')
Solution().lengthOfLongestSubstring('pwwkew')
# Solution().lengthOfLongestSubstring('')
# Solution().lengthOfLongestSubstring('c')
# Solution().lengthOfLongestSubstring('ca')
Solution().lengthOfLongestSubstring('dvdf')
Solution().lengthOfLongestSubstring('anviaj')

