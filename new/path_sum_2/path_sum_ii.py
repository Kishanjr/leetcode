# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """

        self.targetSum = targetSum
        self.result = []
        self.dfs(root, 0, [])
        print(self.result)
        return self.result

    def dfs(self, root, currSum, path):
        if not root:
            return

        currSum += root.val
        path.append(root.val)

        self.dfs(root.left, currSum, path)

        if not root.right and not root.left:
            if self.targetSum == currSum:
                temp = path[:]
                self.result.append(temp)

        self.dfs(root.right, currSum, path)

        path.pop()
