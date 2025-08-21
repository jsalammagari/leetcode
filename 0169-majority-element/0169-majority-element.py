class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {}
        max=len(nums)//2
        for i in range(len(nums)):
            if nums[i] not in hash_map:
                hash_map[nums[i]]=1
            else:
                hash_map[nums[i]]=hash_map[nums[i]]+1
        for key, value in hash_map.items():
            if value>max:
                return key