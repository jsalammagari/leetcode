class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        output = ['']*len(s)
        for i in range(len(indices)):
            output[indices[i]]=s[i]
        return ''.join(output)
