class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        lmax=0
        rmax=0
        ans=0
        while left < right:
            lmax=max(lmax,height[left])
            rmax=max(rmax,height[right])
            if lmax < rmax:
                ans=ans+lmax-height[left]
                left = left+1
            else:
                ans=ans+rmax-height[right]
                right =right-1
        return ans