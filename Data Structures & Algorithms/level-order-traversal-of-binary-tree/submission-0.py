# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        final_list = []
        
        queue = collections.deque([root])

        while queue:
            queue_len = len(queue)
            level_nodes = []
            
            for i in range(queue_len):
                node = queue.popleft()
                level_nodes.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

            final_list.append(level_nodes)
        
        return final_list

        # Time: O(n): going through every node in the tree
        # Space: O(n/2) [max level of a binary tree = n/2] = o(n)