class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected=sorted(heights);
        different=[];
        for i in range(len(heights)):
            if expected[i]!=heights[i]:
                different.append(i);
        return len(different);