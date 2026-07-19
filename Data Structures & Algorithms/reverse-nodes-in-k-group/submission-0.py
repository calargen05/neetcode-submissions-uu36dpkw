'''

UPI Method:

    U - Understand: Reverse nodes in k-long batches. When the list has less than k nodes left
    to be reversed, don't reverse them. Return the head
    P - Plan: I'll have 3 pointers, the curr pointer, the prev pointer, and the check pointer.
    The curr and prev pointers are to iterate through the list and reverse the list in-place
    in batches. The check pointer is to check if the list has enough nodes to perform the
    reverse operation. I'll also keep the rest of the list stored by getting check.next as a
    variable. I'll return the head at the end
    I - Implement: See below ^_^

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # list reverse helper function
        def reverse(cu,pr,n):
            count = 0
            while cu and count < n:
                rest_of_list = cu.next
                cu.next = pr
                pr = cu
                cu = rest_of_list
                count += 1
            return pr
        
        dummy = ListNode(0)
        dummy.next = head
        curr,check = head,head
        prev = None
        
        # loop to iterate through the list (terminate list by setting check to None)
        while check:
            count = 0
            # iterate through list to get the segment to reverse
            while count < k and check:
                check = check.next
                count += 1
            # checking if the end of the list was reached
            if count == k:
                node = reverse(curr,prev,k) # reverse the nodes

                # connect the reversed list to the dummy head on the first iteration
                if curr == head:
                    dummy.next = node
                
                # make the last node of the last group connect to the head of the new reversed
                # group
                else:
                    prev.next = node

                curr.next = check # connect the new reversed group to the rest of the list

                prev = curr # move the pointer to the last node of the last group to the last pointer of
                            # the last node of the new group

                curr = check # move the pointer forward 1 to get pre-reversed head of the next group
            else:
                check = None # terminates the while loop

        return dummy.next # returns the head of the list
