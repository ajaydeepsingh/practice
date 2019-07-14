"""
Note: Try to solve this task in O(n) time using O(1) additional space,
where n is the number of elements in the list, since this is what you'll 
be asked to do during an interview.

Given a singly linked list of integers l and an integer k, 
remove all elements from list l that have a value equal to k.
"""

# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None
#
def removeKFromList(l, k):

    if l is None:
        return l
    elif l.value == k: 
        l = l.next
    
    current = l
    
    while current is not None and current.next is not None: 
        if current.next.value == k:
            current.next = current.next.next
        else:
            current = current.next
            
    if current is not None and current.value == k:
        l = l.next
        
    return l





