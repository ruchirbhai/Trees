# https://leetcode.com/problems/binary-tree-postorder-traversal/

# Given a binary tree, return the postorder traversal of its nodes' values.
# Example:
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# Output: [3,2,1]
# Follow up: Recursive solution is trivial, could you do it iteratively?

class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class Solution:
    def bt_postorder_traversal(self, root):
        if root == None:
            return
        result = []

        def helper(node):
            if node.left is None and node.right is None:
                result.append(node.val)
                return
            
            if node.left is not None:
                helper(node.left)
            
            if node.right is not None:
                helper(node.right)
            
            result.append(node.val)
            
            return
        
        helper(root)
        return result
    
    def bt_postorder_traversal_iterative(self, root):
        if root == None:
            return
        result = []

        stack = [(root,None)]

        while len(stack) != 0:
            (node, zone) = stack[-1]

            if zone == None:
                stack[-1] = (node, "arrival")
                if node.left is not None:
                    stack.append((node.left, None))
            
            elif zone == "arrival":
                stack[-1] = (node, "interim")
                if node.right is not None:
                    stack.append((node.right, None))
            
            elif zone == "interim":
                stack[-1] = (node, "departure")
                result.append(node.val)
                stack.pop()
        return result
        

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

# Create a object for the class
obj = Solution()
#now call the class methos with the needed arguments
print(obj.bt_postorder_traversal(root))
print(obj.bt_postorder_traversal_iterative(root))