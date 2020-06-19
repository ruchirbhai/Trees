# https://leetcode.com/problems/diameter-of-binary-tree/
# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length 
# of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# Example:
# Given a binary tree
#           1
#          / \
#         2   3
#        / \     
#       4   5    
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

# Note: The length of path between two nodes is represented by the number of edges between them.

# -----NOTE---------
# Here neither top down DFS will work nor breath first will work
# Every node has a local problem to solve
# lazy manager approach will not work in every scenario
# consider a case where the longest path does not involve the root node

# two key concepts
# 1. satisfy our parent when we call the recursion by returning the height of the tree
# 2. calculate the local answer from the information coming up from the child
# these two asks are seperate and need to completed individually so 2 tasks get interleaved

from collections import deque

answer = 0

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


class Solution:
    def diameter_binarytree(self, root):
        # edge case if root is null
        if root is None:
            return 0
        global answer
        self.diameter_bt_helper(root)

        return answer

    def diameter_bt_helper(self, node):
        #base case : leaf node
        if node.left is None and node.right is None:
            # here since its the leaf node we return the height as zero and there is no other node below it
            # the local diameter is also zero
            return 0
        # initialize the local heights and diameter
        left_height  = 0
        right_height = 0
        my_diameter  = 0

        # recursive steps
        # since we reach here one of the nodes is non-zero
        if node.left is not None:
            # here the return value will be the left heigth of the subtree
            # we capture this value and pass it on to the parent call
            left_height = self.diameter_bt_helper(node.left)
            # since we finish one iterration we can increment the diameter by 1
            my_diameter = left_height + 1
        
        if node.right is not None:
            # here the return value will be the right heigth of the subtree
            right_height = self.diameter_bt_helper(node.right)
            # here we are checking the v shape we cannot do my_diameter = right_height + 1
            my_diameter += right_height + 1

        my_height = max(left_height, right_height) + 1
        # the global answer needs to be updated if we find a larger v shape tree
        global answer
        if my_diameter > answer:
            answer = my_diameter
        
        # we return my height as that is what the recursion code needs as a return value
        return my_height
        


#driver program for the above function
# #left side of the tree
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
#right side of the tree
root.right = TreeNode(3)


# Create a object for the class
obj = Solution()
#now call the class methos with the needed arguments

print(obj.diameter_binarytree(root))