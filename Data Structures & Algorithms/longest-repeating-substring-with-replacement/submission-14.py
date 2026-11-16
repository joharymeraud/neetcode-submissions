class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = maxf = 0
        for r, c in enumerate(s):
            count[c] = count.get(c, 0) + 1
            maxf = max(maxf, count[c])
            if (r - l + 1) - maxf > k:   # fenêtre invalide : elle glisse d'un cran
                count[s[l]] -= 1
                l += 1
        return len(s) - l