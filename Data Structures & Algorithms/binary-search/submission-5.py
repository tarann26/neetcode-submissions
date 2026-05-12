class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==0:
            return -1
        
        l,r = 0,len(nums)-1
        mid = math.floor((l+r)/2)
        while l <= r:
            if nums[mid]<target:
                l=mid+1
            elif nums[mid]>target:
                r=mid-1
            else:
                return mid
            mid = math.floor((l+r)/2)
        return -1
