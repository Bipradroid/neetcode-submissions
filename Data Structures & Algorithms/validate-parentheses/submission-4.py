class Solution:
    def isValid(self, s: str) -> bool:
        par={
            "(": ")",
            "{": "}",
            "[": "]"
        }
        stack=[]
        if not s:
            return True
        for c in s:
            if stack:
                if stack[-1]=="(" and c==")":
                    stack.pop()
                    continue
                elif stack[-1]=="{" and c=="}":
                    stack.pop()
                    continue
                elif stack[-1]=="[" and c=="]":
                    stack.pop()
                    continue
                else:
                    stack.append(c)
            else:
                stack.append(c)
            
        if stack:
            return False
        else:
            return True
        