# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def height(root):
            nonlocal max_diameter
            if not root:
                return 0
            left_height = height(root.left)
            right_height = height(root.right)

            diameter = left_height + right_height

            max_diameter = max(max_diameter, diameter)

            return 1 + max(left_height, right_height)
        
        height(root)
        return max_diameter

        # Time: O(n) 'cause for each node we are doing constant time operations
        # Space: O(M) M is no. of nodes in the tree 'cause it is doing DFS (going to the bottom and then coming back up so it's keeping the height of the call stack open)

        