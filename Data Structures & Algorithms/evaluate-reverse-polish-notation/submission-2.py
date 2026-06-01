class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in  range(len(tokens)):
            if tokens[i]!="+" and tokens[i]!="-" and tokens[i]!="/" and tokens[i]!="*":
                stack.append(int(tokens[i]))
            elif tokens[i]=="+":
                res=stack[-2]+stack[-1]
                stack.pop()
                stack.pop()
                stack.append(res)
            elif tokens[i]=="-":
                res=stack[-2]-stack[-1]
                stack.pop()
                stack.pop()
                stack.append(res)
            elif tokens[i]=="*":
                res=stack[-2]*stack[-1]
                stack.pop()
                stack.pop()
                stack.append(res)
            elif tokens[i]=="/":
                res=int(stack[-2]/stack[-1])
                stack.pop()
                stack.pop()
                stack.append(res)
        return stack[-1]
