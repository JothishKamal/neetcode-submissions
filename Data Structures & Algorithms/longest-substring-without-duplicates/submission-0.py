class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        w=set()
        res=float('-inf')
        l=0

        for r in range(len(s)):
            while s[r] in w:
                w.remove(s[l])
                l+=1

            w.add(s[r])
            res=max(res,r-l+1)

        return res
