# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next   # keep track of rest of list
            curr.next = prev        # reverse the pointer
            prev = curr             # move prev forward 1 node
            curr = next_node        # move curr forward 1, keep connected to rest of linked list

        return prev                 # the new head