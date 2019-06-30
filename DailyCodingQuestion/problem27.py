# Given a string of round, curly, and square open and closing brackets,
# return whether the brackets are balanced (well-formed).
# For example, given the string "([])[]({})", you should return true.
# Given the string "([)]" or "((()", you should return false.

# stack problem

def wellFormed(inputString):

    if len(inputString) % 2 != 0:
        return False
    
    stack = []

    for x in inputString:
        if (x == '[') or (x == '(') or (x == '{'):
            stack.append(x)
        elif (x == ']'):
            if stack.pop() != '[':
                return False
        elif (x == '}'):
            if stack.pop() != '{':
                return False
        elif (x == ')'):
            if stack.pop() != '(':
                return False
    
    if len(stack) == 0:
        return True
    else:
        return False




print(wellFormed('([)]'))
print(wellFormed('([])'))