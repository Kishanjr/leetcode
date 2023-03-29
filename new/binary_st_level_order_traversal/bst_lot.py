# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#tc -O(N)
# sc - O(N) nis the number of nodes

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        # if root is None, return empty list
        if not root:
            return []

        # initialize the result list with root's value
        result = [[root.val]]

        # create a deque and add the root node
        q = deque()
        q.append(root)

        # loop through the queue till it's empty
        while q:
            # get the number of nodes at this level
            size = len(q)

            # create a list to store values of nodes at this level
            level = []

            # process all nodes at this level
            for _ in range(size):
                node = q.popleft()

                # if node has a left child, add it to queue and level list
                if node.left:
                    q.append(node.left)
                    level.append(node.left.val)

                # if node has a right child, add it to queue and level list
                if node.right:
                    q.append(node.right)
                    level.append(node.right.val)

            # if level list is not empty, add it to result
            if level:
                result.append(level)

        return result
