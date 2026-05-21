class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        max_water=0
        while l<r:
            breadth=r-l
            water= min(heights[l],heights[r])*breadth
            if water > max_water:
                max_water = water
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return max_water