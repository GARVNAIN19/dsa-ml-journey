class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = {}
        left = 0
        result =0
        for right, char in enumerate(s):
            if char in seen and seen[char] >= left:

                left = seen[char] +1
            seen[char] = right
            result = max(result,right - left +1 )
        return result