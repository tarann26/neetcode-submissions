class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        stack = []
        for st in s:
            if st in '({[':
                stack.append(st)
            elif st in ')}]':
                if len(stack) != 0:
                    if st ==')' and stack[-1]=='(':
                        stack.pop()
                    elif st =='}' and stack[-1]=='{':
                        stack.pop()
                    elif st ==']' and stack[-1]=='[':
                        stack.pop()
                    else: 
                        return False
                else:
                    return False
            else:
                continue
        return len(stack) == 0
