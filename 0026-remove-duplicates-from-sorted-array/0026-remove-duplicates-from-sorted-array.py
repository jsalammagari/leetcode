class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        j=i+1
        while i<len(nums):
            if nums[j-1]!=nums[i]:
                nums[j]=nums[i]
                j=j+1
            i=i+1
        return j