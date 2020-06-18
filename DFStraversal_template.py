# DFS traversal template

# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


class Solution:
    results = []

    def dfs_helper(self, node):
        # Base Case
        if node.left is None and node.right is None:
            #leaf level processing
            return
        #Now we traverse through the left side of the tree and then the right
        if node.left is not None:
            self.dfs_helper(node.left)
        
        # right side 
        if node.right is not None:
            self.dfs_helper(node.right)
        
        return

    def dftraversal(self, root):
        # Here there a difference between recursion and trees where we need to check if the root 
        # is Null right at the start before calling recursion 
        if root is None:
            return
        
        # ensure you use self.fuunction to call another function in the same class
        self.dfs_helper(root)

        return
    



#driver program for the above function

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Create a object for the class
obj = Solution()
#now call the class methos with the needed arguments

obj.dftraversal(root)