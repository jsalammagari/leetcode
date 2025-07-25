class Solution:
    def reverseSubstrings(self, chars, left, right):
        while left < right:
            chars[left],chars[right]=chars[right],chars[left]
            left = left+1
            right=right-1
    def reverseWords(self, s: str) -> str:
        chars=list(s)
        n = len(chars)
        start = 0
        for end in range(n+1):
            if end==n or chars[end]==' ':
                self.reverseSubstrings(chars,start,end-1)
                start = end+1
        return ''.join(chars)

        