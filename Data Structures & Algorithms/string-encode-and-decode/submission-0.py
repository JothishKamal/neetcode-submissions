class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = ""
        for s in strs:
            res += s + "‎"
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        s = s.split("‎")
        return s[:len(s)-1]
