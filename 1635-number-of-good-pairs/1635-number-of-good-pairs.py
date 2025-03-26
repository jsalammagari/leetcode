class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums);
        result=0;
        for freq in count.values():
            result= result+freq*(freq-1)//2;
        return result;
