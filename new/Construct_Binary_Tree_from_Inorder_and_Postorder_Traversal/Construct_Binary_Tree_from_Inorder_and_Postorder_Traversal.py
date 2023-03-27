# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        if not preorder:
            return None

        rootElement = preorder[0]
        root = TreeNode(rootElement)

        for i in range(len(inorder)):
            if inorder[i] == rootElement:
                pivot = i
                break

        root.left = self.buildTree(preorder[1:pivot+1], inorder[:pivot])
        root.right = self.buildTree(preorder[pivot+1:], inorder[pivot+1:])

        return root
