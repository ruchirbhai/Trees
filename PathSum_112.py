# https://leetcode.com/problems/path-sum/
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such 
# that adding up all the values along the path equals the given sum.

# Note: A leaf is a node with no children.
# Example:
# Given the below binary tree and sum = 22,
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

from collections import deque

answer = False
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


class Solution:
    def path_sum(self, root):
        # Edge case when the root is empty
        if root is None:
            # if the target is Zero and the tree is null its not clear if we return true of false.
            # another corner case to consider
            return False
        global answer

        self.path_sum_helper(root, 0, 22)

        return answer
    
    def path_sum_helper(self, node, slate_sum, target):
        #base case: leaf node
        if node.left is None and node.right is None:
            if slate_sum + node.data == target:
                global answer 
                answer = True
                return answer
        
        # recursive case
        if node.left is not None:
            self.path_sum_helper(node.left, slate_sum + node.data, target)
        
        #right side
        if node.right is not None:
            self.path_sum_helper(node.right, slate_sum + node.data, target)
        



#driver program for the above function
# #left side of the tree
# root = TreeNode(1)
root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
#right side of the tree
root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

# Create a object for the class
obj = Solution()
#now call the class methos with the needed arguments

print(obj.path_sum(root))