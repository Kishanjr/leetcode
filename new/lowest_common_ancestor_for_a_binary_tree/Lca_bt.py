Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# TC - O(n) because we  visits each node in the tree exactly once, in the worst case
# SC - O(n) consider the worst case the  reccuresive call stack may be  size of n

class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # We Call the dfs function
        return self.dfs(root, p, q)

    def dfs(self, root, p, q):
        # Base case: if the root is None, We return None.
        if root == None:
            return None

        # If either p or q is equal to the root, then the LCA is the root itself .
        if p.val == root.val or q.val == root.val:
            return root

        # We Recursively search the left subtree for p and q.
        left_side = self.dfs(root.left, p, q)

        # We Recursively search the right subtree for p and q.
        right_side = self.dfs(root.right, p, q)

        # If only one side contains a valid node, return that side.
        if left_side == None:
            return right_side
        if right_side == None:
            return left_side

        # If p and q are on different sides of the current node, the current node is the LCA.
        return root
