

class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        queue = deque()
        
        for w in wordDict:
            l = len(w)
            if s[0:l] == w:
                queue.append(l-1)
        seen = set()
        while queue:            
            for _ in range(len(queue)):
                node = queue.popleft()

                if node == len(s)-1:
                    return True

                for w in wordDict:
                    if s[node+1:node+len(w)+1] == w:
                        if node+len(w) not in seen:
                            queue.append(node+len(w))
                            seen.add(node+len(w))
                        
        return False

        
        