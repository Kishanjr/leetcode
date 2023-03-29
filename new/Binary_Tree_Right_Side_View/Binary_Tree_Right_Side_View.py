# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Time Complexity: O(n), where n is the number of nodes in the tree. We traverse each node once.

# Space Complexity: O(d), where d is the maximum number of nodes at any level.

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        result = []
        q = deque()
        q.append(root)

        while q:

            size = len(q)
            level = []

            for i in range(size):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(level[-1])
        return result
