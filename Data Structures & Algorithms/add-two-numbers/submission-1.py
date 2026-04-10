# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # carry variable to keep track of sums that are greater than 10 between 2 digits
        carry = 0

        # linked list creation and current pointer definition
        res = ListNode()
        current = res


        # loop to calculate the value of the sums between every pair of nodes
        while l1 or l2 or carry:
            # values of the nodes in the 2 linked lists
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # value and carry calculation
            value = v1 + v2 + carry
            carry = (value)//10
            value = value % 10
            """ 
            assigning the next node of the new linked list the current value
            because the head node of the linked list isn't able to store a value
            """
            current.next = ListNode(value)

            """
            iterating the pointers to get to the next node of each linked list
            if they have one
            """
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return res.next
