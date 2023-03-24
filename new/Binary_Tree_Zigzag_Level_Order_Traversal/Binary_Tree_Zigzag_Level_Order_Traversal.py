# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Check if root is empty, return empty list
        if not root:
            return []

        # Create a result list and add the root node value as first level
        res = [[root.val]]

        # Create a deque data structure and add root node
        q = deque([root])

        # Iterate over deque
        while q:
            # Get the size of the deque
            size = len(q)

            # Create an empty list to store node values for this level
            level = []

            # Iterate over each node in the deque at this level
            for i in range(size):
                # Remove the first node from the deque
                node = q.popleft()

                # Check if the node has a left child, add to deque and level list
                if node.left:
                    q.append(node.left)
                    level.append(node.left.val)

                # Check if the node has a right child, add to deque and level list
                if node.right:
                    q.append(node.right)
                    level.append(node.right.val)

            # Check if there were any nodes at this level
            if level:
                # Check if the level is odd, reverse the list and append to result list
                if len(res) % 2:
                    res.append(reversed(level))
                # If level is even, append the level list to result list as is
                else:
                    res.append(level)

        # Return the result list
        return res
