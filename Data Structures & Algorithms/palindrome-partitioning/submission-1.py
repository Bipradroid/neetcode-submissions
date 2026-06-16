class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        # Store all palindrome ranges (start, end)
        pal = set()

        # Odd-length palindromes
        for i in range(n):
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                pal.add((l, r))
                l -= 1
                r += 1

        # Even-length palindromes
        for i in range(n):
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                pal.add((l, r))
                l -= 1
                r += 1

        res = []
        part = []

        def dfs(start):
            if start == n:
                res.append(part.copy())
                return

            for end in range(start, n):
                if (start, end) in pal:
                    part.append(s[start:end + 1])
                    dfs(end + 1)
                    part.pop()

        dfs(0)
        return res
        