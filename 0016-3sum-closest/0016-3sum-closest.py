class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        sum =0
        nums.sort()
        for i in range(len(nums)):
            low= i+1
            high= len(nums)-1
            while low<high:
                sum = nums[i]+nums[low]+nums[high]
                if abs(target-sum)<abs(diff):
                    diff = target -sum
                if sum < target:
                    low=low+1
                else:
                    high=high-1
            if diff==0:
                break
        return target-diff