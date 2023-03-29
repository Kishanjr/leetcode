# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# TC-O(N^2)
# SC-O(N)

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        # If the preorder list is empty, return None
        if not preorder:
            return None

        # The first element in the preorder list is the root node
        rootElement = preorder[0]

        # Create a new TreeNode object with the root element value
        root = TreeNode(rootElement)

        # Find the pivot index in the inorder list, which separates left and right subtrees
        for i in range(len(inorder)):
            if inorder[i] == rootElement:
                pivot = i
                break

        # Recursively build the left and right subtrees
        # The left subtree is built from the first elements of preorder and inorder up to the pivot index
        root.left = self.buildTree(preorder[1:pivot+1], inorder[:pivot])
        # The right subtree is built from the remaining elements of preorder and inorder after the pivot index
        root.right = self.buildTree(preorder[pivot+1:], inorder[pivot+1:])

        # Return the root of the resulting binary tree
        return root
