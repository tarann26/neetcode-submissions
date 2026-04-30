class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        n = len(num)
        if n==0:
            return []
        i,j=0,n-1
        while i<j:
            if num[i]+num[j] == target:
                return [i+1,j+1]
            elif num[i]+num[j] < target:
                i+=1
            else: 
                j-=1
        return []