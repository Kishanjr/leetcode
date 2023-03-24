# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []
        result = [[root.val]]
        q = deque()
        q.append(root)
        while q:
            size = len(q)
            # create level list to add level wise processing
            level = []

            for _ in range(size):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                    level.append(node.left.val)

                if node.right:
                    q.append(node.right)
                    level.append(node.right.val)
            if level:
                result.append(level)

        return result
