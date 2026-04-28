# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Floyd's cycle finding algorithm
        
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False

        # Time: O(n): before the cycle: We traverse the non-cyclical part of the list, which takes O(n) time.
        # Inside the cycle: Once both pointers are in the cycle, they will meet after a constant number of steps, taking O(k) time. Since k is bounded (the length of the cycle), this is effectively a constant.
        # Space: O(1): no extra space except the two pointers slow and fast