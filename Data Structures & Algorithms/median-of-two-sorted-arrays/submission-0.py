class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=sorted((nums1+nums2))
        l,r=0,len(nums)-1
        
        if len(nums)%2!=0:
            return nums[(l+r)//2]
        else:
            avg=(nums[(l+r)//2]+nums[((l+r)//2)+1])/2
            return avg
        