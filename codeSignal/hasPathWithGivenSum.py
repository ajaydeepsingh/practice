#
# Given a binary tree t and an integer s, determine whether there is a root to 
# leaf path in t such that the sum of vertex values equals s.



# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

def hasPathWithGivenSum(t, s):
    if not t:
        return False
    
    if not t.left and not t.right and t.value == s:
        return True
    
    s -= t.value

    return hasPathWithGivenSum(t.left, s) or hasPathWithGivenSum(t.right, s)

