# https://leetcode.com/problems/path-sum-ii/
# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
# Note: A leaf is a node with no children.

# Example:
# Given the below binary tree and sum = 22,
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1
# Return:
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]


from collections import deque

answer = []

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


class Solution:
    def path_sum_2(self, root):
        if root is None:
            return
        
        self.path_sum_2_helper(root,[],22)

        global answer
        return answer

    def path_sum_2_helper(self, node, slate, target):
        # Base case
        if node.left is None and node.right is None:
            if sum(slate) + node.data == target:
                global answer
                slate.append(node.data)
                answer.append(slate[:])
                slate.pop()
                return
        
        # recursion
        # append the node value in the slate list
        slate.append(node.data)
        #left side
        if node.left is not None:
            self.path_sum_2_helper(node.left, slate, target)
        
        #right side
        if node.right is not None:
            self.path_sum_2_helper(node.right, slate, target)
        
        # pop the appened value once the recursion is complete
        slate.pop()




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
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)

# Create a object for the class
obj = Solution()
#now call the class methos with the needed arguments

print(obj.path_sum_2(root))