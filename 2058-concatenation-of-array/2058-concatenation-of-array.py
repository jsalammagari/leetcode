class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # n=len(nums);
        # ans=nums+nums;
        # return ans;
        n=len(nums);
        ans=[];
        for i in range(0,2*n):
            ans.append(nums[i%n]);
        return ans;
