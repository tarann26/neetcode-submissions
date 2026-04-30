class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n==0:
            return []
        l = {}
        for i in nums:
            if i in l:
                l[i]+=1
            else: 
                l[i]=1
        s = sorted(l.items(), key=lambda x: x[1], reverse=True)
        y = [s[t][0] for t in range(k)]
        return y
 