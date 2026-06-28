# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz = 0

        # getting the size of the LL
        curr = head
        while curr:
            sz += 1
            curr = curr.next
        
        target = sz - n
        if target == 0:
            return head.next
        count = 1

        curr = head
        while curr:
            if count == target:
                if curr.next:
                    curr.next = curr.next.next
                    break
            else:
                count += 1
                curr = curr.next
        
        return head