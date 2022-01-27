class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = {}
        ans = 0
        i = 0 # sliding window

        for j in range(len(s)):
            chr = s[j]

            if (chr in counter):
                i = max(counter[chr], i)

            ans = max(ans, j + 1 - i)
            counter[chr] = j + 1
        
        return ans

# test here
print(Solution().lengthOfLongestSubstring('dvdf'))
