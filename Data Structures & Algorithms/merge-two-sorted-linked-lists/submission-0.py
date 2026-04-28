# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy_node = ListNode()
        tail = dummy_node

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if not list1:
            tail.next = list2
        if not list2:
            tail.next = list1
        
        return dummy_node.next

        # Time: O(n + m) n, m = len of list1, list2 'cause we are going through each elem of both lists in worst case
        # Space: O(1) just creating dummy, tail as extra pointers so O(1)

        
        