class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=2
        j=2
        while i < len(nums):
            if nums[j-2]!=nums[i]:
                nums[j]=nums[i]
                j=j+1
            i=i+1
        return j