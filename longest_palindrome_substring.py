class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            s1 = ""
            for j in range(i, len(s)):
                s1 = s1 + s[j]
                if s1 == s1[::-1] and len(s1) > len(ans):
                    ans = s1
        return ans
