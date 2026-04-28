# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True

        def height(root):
            nonlocal balanced
            if not root:
                return 0
            left_height = height(root.left)
            if not balanced:
                return 0
            right_height = height(root.right)

            if abs(left_height - right_height) > 1:
                balanced = False
            
            return 1 + max (left_height, right_height)
        
        height(root)
        return balanced

    # Time : O(n) visiting each node and doing constant time operations for each node
    # Space: O(H) H is height of the tree 'cause it is doing DFS (going to the bottom and then coming back up so height of call stack is max depth / height of tree) 
        