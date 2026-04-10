# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        
        l1 = list1
        l2 = list2

        head = ListNode(0)

        if l1.val <= l2.val:
            head.val = list1.val
            l1 = l1.next
        else:
            head.val = list2.val
            l2 = l2.next
        
        curr = head

        while l1 or l2:

            if l1 and l2 and l1.val <= l2.val:
                curr.next = ListNode(l1.val)
                l1 = l1.next
            elif l1 and not l2:
                curr.next = ListNode(l1.val)
                l1 = l1.next
            elif l2:
                curr.next = ListNode(l2.val)
                l2 = l2.next
            if curr:
                curr = curr.next

        return head
