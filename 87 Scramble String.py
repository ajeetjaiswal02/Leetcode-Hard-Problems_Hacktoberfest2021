class Solution:
    @lru_cache
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1)<3: return Counter(s1)==Counter(s2)
        res1=res2=False
        for i in range(1,len(s1)):
            if Counter(s1[:i])==Counter(s2[:i]):
                res1=self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:])
            if Counter(s1[:i])==Counter(s2[-i:]):
                res2= self.isScramble(s1[:i],s2[-i:]) and self.isScramble(s1[i:],s2[:-i])
            if res1 or res2: return True
        return False
