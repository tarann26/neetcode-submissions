class Solution:
    def trap(self, h: List[int]) -> int:
        if len(h) == 0:
            return 0
        n = len(h)
        l = [0] * n
        l[0] = h[0]
        r = [0] * n

        for i in range(1,n):
            l[i] = max(l[i-1], h[i])

        r[n-1] = h[n-1]
        for i in range(n-2,-1, -1):
            r[i] = max(r[i+1], h[i])

        vol = 0
        for i in range(n):
            vol += min(l[i],r[i]) - h[i]

        return vol






            
