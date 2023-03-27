class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.result = 0
        self.k = k
        self.inorder(root)
        return self.result

    def inorder(self, root):
        if not root:
            return

        self.inorder(root.left)
        self.k -= 1
        if self.k == 0:
            self.result = root.val
        self.inorder(root.right)
