# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
# Given a binary tree, return the bottom-up level order traversal of its 
# nodes' values. (ie, from left to right, level by level from leaf to root).
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]

from collections import deque

class TreeNode:
    def __init__(self, key):
        self.val   = key
        self.left  = None
        self.right = None

class Solution:
    def bst_bottom_up(self,root):
        answer = []
        answer = self.helper(root)
        
        return answer[::-1]
    
    def helper(self, root):
        # Base case
        if root.left is None and root.right is None:
            return
        result = []
        q = deque([root])

        while len(q) != 0:
            numnodes = len(q)
            temp = []

            for _ in range(numnodes):
                node = q.popleft()
                temp.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                
            result.append(temp)
        
        return result




root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Create a object for the class
obj = Solution()
#now call the class methos with the needed arguments
print(obj.bst_bottom_up(root))


