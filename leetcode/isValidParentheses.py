def isValidParentheses(s):
    if len(s) % 2 != 0:
        return False

    if len(s) == 0:
        return True

    if (s[0] == ']') or (s[0] == ')') or (s[0] == '}'):
        return False

    stack = []

    for x in s:
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
