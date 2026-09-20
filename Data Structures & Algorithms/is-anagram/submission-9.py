class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_freq = Counter(s)
        t_freq = Counter(t)
        if s_freq != t_freq:
            return False
        return True