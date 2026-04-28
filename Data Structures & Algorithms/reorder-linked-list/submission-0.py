# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # do fast, slow to find mid point
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # splitting the list
        second = slow.next # second half of the list

        # setting the next pointer of the last node of the first list (which will eventually be the final last node) to null ptr
        slow.next = None

        # reversing the second half
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # merging two halves
        first = head
        second = prev

        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        
        # Time: O(n)
        # Space: O(1)