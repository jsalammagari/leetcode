class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for index_i,value_i in enumerate(nums):
            remainder_value = target - value_i
            if remainder_value in map:
                return [index_i,map[remainder_value]]
            else:
                map[value_i] = index_i