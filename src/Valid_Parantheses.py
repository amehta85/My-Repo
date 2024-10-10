class Solution(object):
    def isValid(self, s):
        stack = [] #Initialize empty list to track opening brackets
        mapping = {')': '(', '}': '{', ']': '['} #creating dictionary with Key+Value pairs where closing brackets are the keys and their opening brackets are values
        
        for char in s:
            if char in mapping.values():  # check if it's one of '(', '{', '['
                stack.append(char)    #if its opening bracket push to stack
            elif char in mapping.keys():  # else check if it's one of ')', '}', ']'
                if stack and stack[-1] == mapping[char]: # check if the stack is not empty and the top of the stack matches closing bracket
                    stack.pop()  # remove the top item from the stack as it forms a valid pair with the current closing bracket.
                else:
                    return False # else if stack is empty or the top of the stack doesn’t match the opening bracket then False
        return not stack    #check if stack is empty, all parentheses were matched properly


        