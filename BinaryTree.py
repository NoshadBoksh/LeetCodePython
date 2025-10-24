# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.maxSum = float('-inf')  # Initialize global max
        
        def dfs(node):
            if not node:
                return 0

            # Compute max path sum for left and right subtrees
            left = max(dfs(node.left), 0)   # ignore negatives
            right = max(dfs(node.right), 0)

            # Check max path passing through this node
            current_path = node.val + left + right
            self.maxSum = max(self.maxSum, current_path)

            # Return max gain from this node to parent
            return node.val + max(left, right)
        
        dfs(root)
        return self.maxSum
