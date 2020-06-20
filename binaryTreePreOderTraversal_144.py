# https://leetcode.com/problems/binary-tree-preorder-traversal/
# Given a binary tree, return the preorder traversal of its nodes' values.

# Example:
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
# Output: [1,2,3]
# Follow up: Recursive solution is trivial, could you do it iteratively?

class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class Solution:
    def bt_preorder_traversal(self, root):
        if root is None:
            return None
        
        result = []
    
        def helper(node):
            if node.left is None and node.right is None:
                result.append(node.val)
                return
            
            #preorder traversal you need to append at the start
            result.append(node.val)

            if node.left is not None:
                helper(node.left)
            
            if node.right is not None:
                helper(node.right)
            
        helper(root)
        return result

    def bt_preorder_traversal_iterative(self, node):
        if node is None:
            return None
        
        result = []

        stack = [(node, None)]

        while len(stack) != 0:
            (node, zone) = stack[-1]

            if zone is None:
                stack[-1] = (node, "arrival")
                result.append(node.val)
                if node.left is not None:
                    stack.append((node.left, None))
            
            elif zone == "arrival":
                stack[-1] = (node, "interim")
                if node.right is not None:
                    stack.append((node.right, None))
            
            elif zone == "interim":
                stack[-1] = (node, "departure")
                stack.pop()
        
        return result



root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

# Create a object for the class
obj = Solution()
#now call the class methos with the needed arguments
print(obj.bt_preorder_traversal(root))
print(obj.bt_preorder_traversal_iterative(root))