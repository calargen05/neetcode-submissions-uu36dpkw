# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
UPI Method:
    U - Understand: The problem wants me to take an arbitrary number of linked
    lists and sort them into one large linked list
    P - Plan: I will use base cases to have solutions to the length of one and
    zero cases. I will start with the first linked list and then loop through
    the other lists to get the new numbers and I'll insert them into the linked
    list to keep the final list sorted in ascending order. Then, I'll return the
    final list
    I - Implement: see below VVV
"""


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # base cases
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        # create a dummy head node for the final linked list
        head = ListNode()

        # loop to get each linked list
        for l in lists:
            curr = l

            # loop to get each node of the list
            while curr:
                m_curr = head
                # get the spot to insert the current value of the linked list
                # into the merged linked list
                while m_curr.next != None:
                    if m_curr.next.val > curr.val:
                        break
                    m_curr = m_curr.next

                # insert the value into the spot on the merged linked list
                if not m_curr.next:
                    m_curr.next = ListNode(curr.val)
                    curr = curr.next
                else:
                    nextnode = ListNode(curr.val)
                    original_next = m_curr.next
                    m_curr.next = nextnode
                    m_curr.next.next = original_next
                    curr = curr.next

        # return the head of the merged linked list                
        return head.next
