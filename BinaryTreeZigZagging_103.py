# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# Given a binary tree, return the zigzag level order traversal of its nodes' values. 
# (ie, from left to right, then right to left for the next level and alternate between).
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]

from collections import deque

class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class Solution:
    def bin_tree_zigzag(self, root):
        
        return self.helper(root)
    
    def helper(self, root):
        if root is None:
            return []
        q = deque([root])
        result = []
        reverse_toggle = False

        while len(q) != 0:
            numnodes = len(q)
            tmp = []

            for _ in range(numnodes):
                node = q.popleft()
                tmp.append(node.val)

                if node.left is not None:
                    q.append(node.left)

                if node.right is not None:
                    q.append(node.right)

            if reverse_toggle == False:
                result.append(tmp)
                reverse_toggle = True
            else:
                tmp.reverse()
                result.append(tmp)
                reverse_toggle = False

        return result

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Create a object for the class
obj = Solution()
#now call the class methos with the needed arguments
print(obj.bin_tree_zigzag(root))        


