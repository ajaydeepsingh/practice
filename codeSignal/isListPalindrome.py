# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
d# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def isListPalindrome(l):
    # Edgecase 
    # 
    if l is None:
        return True
    
    if l.next == None:
        return True

    # traverse the list and add to an array
    values = []

    curNode = l
    while curNode is not None:
        values.append(curNode.value)
        curNode = curNode.next

    # Reverse the array and create a new LL
    
    head = ListNode(values[0])
    for x in range(1, len(values)):
        addNode = ListNode(values[x])
        addNode.next = head
        head = addNode

    one = l
    two = head
    
    while one != None and two != None:
        if (one.value != two.value):
            return False

        one = one.next
        two = two.next

    return True