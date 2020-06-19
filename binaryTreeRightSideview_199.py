# https://leetcode.com/problems/binary-tree-right-side-view/
# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Example:

# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:

#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---

from collections import deque

class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class Solution:
    def bintree_rightside_view(self, root):
        return self.helper(root)
    
    def helper(self, root):
        result = []
        q = deque([root])

        
        while len(q) != 0:
            numnodes = len(q)
            tmp = []

            for _ in range(numnodes):
                node = q.popleft()
                if node.left is not None:
                    q.append(node.left)

                if node.right is not None:
                    q.append(node.right)
                tmp.append(node.val)
            
            result.append(tmp[-1])
        
        return result
            


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Create a object for the class
obj = Solution()
#now call the class methos with the needed arguments
print(obj.bintree_rightside_view(root))