class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decompressedList =[];
        for i in range(0,len(nums),2):
            freq=nums[i];
            val=nums[i+1];
            decompressedList.extend([val] * freq);
        return decompressedList;

