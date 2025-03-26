class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = [];
        output.append(nums[0]);
        for i in range(1,len(nums)):
            output.append(nums[i]+output[i-1]);
        return output;
