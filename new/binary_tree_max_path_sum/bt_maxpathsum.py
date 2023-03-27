# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.maximum = root.val
        self.dfs(root)
        return self.maximum

    def dfs(self, root):
        # base
        if not root:
            return 0
            # choose leftsum, Nochoose
        leftSum = max(self.dfs(root.left), 0)
        rightSum = max(self.dfs(root.right), 0)

        rootSum = leftSum + rightSum + root.val

        self.maximum = max(self.maximum, rootSum)

        return max(leftSum, rightSum) + root.val
