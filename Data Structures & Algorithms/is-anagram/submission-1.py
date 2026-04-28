class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=dict(Counter(s))
        b=dict(Counter(t))
        return a==b