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
        # Initialize the target sum and result list
        self.targetSum = targetSum
        self.result = []

        # Perform a depth-first search on the binary tree
        self.dfs(root, 0, [])

        # Print the result and return it
        print(self.result)
        return self.result

    def dfs(self, root, currSum, path):
        # If the current node is empty, return
        if not root:
            return

        # Calculate the current sum and append the node's value to the path
        currSum += root.val
        path.append(root.val)

        # Recursively call the function on the left and right subtrees
        self.dfs(root.left, currSum, path)
        self.dfs(root.right, currSum, path)

        # If the current node is a leaf node, check if the path sum is equal to the target sum
        if not root.right and not root.left:
            if self.targetSum == currSum:
                # If it is, make a copy of the path list and append it to the result list
                temp = path[:]
                self.result.append(temp)

        # Remove the last element from the path list before backtracking
        path.pop()


# tc o(n)
# sc O(nlogn) in the worst case, where n is the number of nodes in the binary tree.
