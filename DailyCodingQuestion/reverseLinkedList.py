def reverseLinkedList(head):


    prev = None
    curr = head
    nxt = None

    while curr != None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    head = prev
