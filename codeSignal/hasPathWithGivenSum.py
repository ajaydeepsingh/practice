"""
Given a binary tree t and an integer s, determine whether there is a root to 
leaf path in t such that the sum of vertex values equals s.
"""


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

"""
Base case
This question wants to find a path from node to the leaf, so the node who 
satisfies must be a leaf (not node.left and not nood.right)

I want to recursively subtract the sum by current node's value, so the leaf 
node of correct path must have the same value of its assigned sum

Recursive step
We want to traverse all the nodes, so node.left and node.right must be 
called parallelly

One valid path is enough, so we want to use or to connect two "branches"
Considering each node as the root of its children, sum should be modified 
from its parent
"""