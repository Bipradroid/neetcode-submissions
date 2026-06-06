class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = {}
        size = 0
        end = 0
        output = []
        for i in range(len(s) - 1, -1, -1):
            if s[i] in hashmap:
                continue
            hashmap[s[i]] = i

        for i, c in enumerate(s):
            size += 1
            end = max(end, hashmap[c])

            if i == end:
                output.append(size)
                size = 0

        return output
        