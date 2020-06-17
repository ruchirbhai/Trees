# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
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


# tree = deque(['3','9','20','15','7'])

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


class Solution:
    # def levelOrder(self, root: TreeNode) -> List[List[int]]:
    
    def function_bfs(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # Edge case where the the input is empty
        if root is None:
            return
        
        #create the result queue
        result = []

        q = deque([root])

        while len(q) != 0:      # While queue is not empty
            numnodes = len(q)   # Record how many nodes are in the current level
            temp = []

            # We have to pop those many nodes. Note that new nodes in the next level will get pushed in the end
            for _ in range(numnodes):
                node = q.popleft()
                # temp array stores all the values in the current level
                temp.append(node.data)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            
            result.append(temp)     # take all collected values and append them to the result array
        
        return result

#driver program for the above function

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Create a object for the class
obj = Solution()
#now call the class methos with the needed arguments
print(obj.function_bfs(root))