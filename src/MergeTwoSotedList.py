class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        #starting point of the merged list
        dummy = ListNode(0)
        current = dummy
        
        # two pointers for list1 and list2
        p1 = list1
        p2 = list2
        
        # Travel both lists until one of them is exhausted
        while p1 and p2:
            if p1.val <= p2.val:
                current.next = p1
                p1 = p1.next
            else:
                current.next = p2
                p2 = p2.next
            current = current.next
        
        # One of the lists might still have remaining elements
        if p1:
            current.next = p1
        else:
            current.next = p2
        
        # Return the merged list, which starts at dummy.next
        return dummy.next
