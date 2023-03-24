"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# Definition for a Node.


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # Check if root is empty, return empty list
        if not root:
            return []

        # Create a deque to use as a queue and add the root node to it
        queue = deque()
        res = [[root.val]]
        queue.append(root)

        # Continue while there are nodes in the queue
        while queue:
            # Get the size of the queue at this level
            size = len(queue)
            # Create an empty list to store node values for this level
            level = []
            # Iterate over each node in the queue at this level
            for i in range(size):
                # Remove the first node from the queue
                node = queue.popleft()
                # Iterate over each child node of the current node
                for child in node.children:
                    # Add the child node to the queue and level list
                    queue.append(child)
                    level.append(child.val)
            # Check if there were any nodes at this level
            if level:
                # Add the level list to the result list
                res.append(level)

        # Return the result list
        return res
