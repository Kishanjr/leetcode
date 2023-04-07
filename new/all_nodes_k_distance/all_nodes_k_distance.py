# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Tc - O(N)
# Sc - O(N)


class Solution(object):
    # Define the distanceK function that takes in the root of the binary tree, the target node and the distance K.
    def distanceK(self, root, target, k):
        # Create an empty dictionary adj that will store the adjacency list for each node in the binary tree.
        adj = {root: []}
        # Create an empty queue q that will store the nodes to be processed in a BFS traversal.
        q = deque()
        # Add the root node to the queue.
        q.append(root)

        # Perform a BFS traversal of the binary tree and populate the adjacency list.
        while q:
            # Pop the first node from the queue.
            node = q.popleft()
            # If the node has a left child, add it to the adjacency list and enqueue it.
            if node.left:
                adj[node].append(node.left)
                adj[node.left] = [node]
                q.append(node.left)
            # If the node has a right child, add it to the adjacency list and enqueue it.
            if node.right:
                adj[node].append(node.right)
                adj[node.right] = [node]
                q.append(node.right)

        # Create a new queue q that will store the nodes to be processed in the second BFS traversal.
        q = deque()
        # Add the target node to the queue.
        q.append(target)
        # Create an empty set visited that will store the nodes that have already been visited.
        visited = set()

        # Perform a BFS traversal of the binary tree starting from the target node and stopping at distance K.
        while q and k > 0:
            # Get the number of nodes in the current level of the BFS traversal.
            size = len(q)
            # Process each node in the current level of the BFS traversal.
            for _ in range(size):
                # Pop the first node from the queue.
                node = q.popleft()
                # Add the node to the visited set.
                visited.add(node)
                # For each neighbor of the node that has not been visited yet, add it to the queue.
                for neigh in adj[node]:
                    if neigh not in visited:
                        q.append(neigh)
            # Decrement k by 1 to move to the next level of the BFS traversal.
            k -= 1

        # Create a list result that will store the nodes at distance K from the target node.
        result = []
        # Add each node in the queue to the result list.
        for ele in q:
            result.append(ele.val)

        # Return the result list.
        return result
