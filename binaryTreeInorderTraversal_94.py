
# https://leetcode.com/problems/binary-tree-inorder-traversal/
# Given a binary tree, return the inorder traversal of its nodes' values.

# Example:

# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# Output: [1,3,2]
# Follow up: Recursive solution is trivial, could you do it iteratively?

class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class Solution:
    def bt_inorder_traversal(self, root):
        if root == None:
            return
        
        result = []

        def helper(node):
            if node.left is None and node.right is None:
                result.append(node.val)
                return

            if node.left is not None:
                helper(node.left)

            result.append(node.val)

            if node.right is not None:
                helper(node.right)
            
            return
        helper(root)
        return result

    def bt_inorder_traversal_iterative(self, root):
        if root == None:
            return
        
        result = []

        stack = [(root,None)]

        while len(stack) != 0:
            (node,zone) = stack[-1]

            if zone is None:
                stack[-1] = (node,"arrival")
                if node.left is not None:
                    stack.append((node.left, None))
            
            elif zone == "arrival":
                stack[-1] = (node, "interim")
                result.append(node.val)
                if node.right is not None:
                    stack.append((node.right, None))
            
            elif zone == "interim":
                stack[-1] = (node,"departure")
                stack.pop()
            
        return result




root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

# Create a object for the class
obj = Solution()
#now call the class methos with the needed arguments
print(obj.bt_inorder_traversal(root))
print(obj.bt_inorder_traversal_iterative(root))