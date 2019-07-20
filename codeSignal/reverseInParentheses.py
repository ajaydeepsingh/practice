"""
Write a function that reverses characters in (possibly nested) parentheses in 
the input string.

Input strings will always be well-formed with matching ()s.


"(bar)" -> "rab"
"foo(bar)baz" -> "foorabbaz"
"foo(bar)baz(blim)" -> "foorabbazmilb"

"""

def reverseInParentheses(inputString):

    stack = []

    for x in inputString:
        if x == ")":
            temp = ""
            while stack[-1] != "(":
                temp += stack.pop()
            stack.pop()

            for item in temp:
                stack.append(item)
        else:
            stack.append(x)

    return "".join(stack)
