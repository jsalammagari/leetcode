class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        n = len(s)
        i=0
        map = {}
        for j in range(n):
            if s[j] in map:
                i =max(map[s[j]],i)
            ans = max(ans,j-i+1)
            map[s[j]]=j+1
        return ans
