class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums);
        num_map={};
        for i,num in enumerate(sorted_nums):
            if num not in num_map:
                num_map[num]=i;
        return [num_map[num] for num in nums];