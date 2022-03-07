class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        res_len = 0

        for i in range(len(s)):
            # odd
            res, res_len = self.checkPalindrome(s, i, i, res, res_len)
            # even
            res, res_len = self.checkPalindrome(s, i, i + 1, res, res_len)

        return res
    
    def checkPalindrome(self, s, l, r, res, res_len):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > res_len:
                res = s[l:r + 1]
                res_len = r - l + 1
            
            l -= 1
            r += 1
        
        return (res, res_len)

# test here
print(Solution().longestPalindrome("b"))
