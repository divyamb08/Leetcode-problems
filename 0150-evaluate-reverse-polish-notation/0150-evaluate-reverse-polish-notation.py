class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ls = []
        for i in range(len(tokens)):
            if tokens[i]=="+":
                ls.append(ls.pop()+ls.pop())

            elif tokens[i]=="-":
                a,b = ls.pop(), ls.pop()
                ls.append(b-a)
            elif tokens[i]=="/":
                a,b = ls.pop(), ls.pop()
                ls.append(int(b/a))

                
            elif tokens[i]=="*":
                ls.append(ls.pop()*ls.pop())

            else:
                ls.append(int(tokens[i]))
        return ls[0]