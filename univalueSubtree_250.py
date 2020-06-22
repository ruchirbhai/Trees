# https://leetcode.com/articles/count-univalue-subtrees/
# Given a binary tree, count the number of uni-value subtrees.

# A Uni-value subtree means all nodes of the subtree have the same value.

# Example :

# Input:  root = [5,1,5,5,5,null,5]

#               5
#              / \
#             1   5
#            / \   \
#           5   5   5

# Output: 4, because each leaf node is a univalue tree and then 5\5 on the right is univalue

# Here top down approach wont work as we need the information for the entire tree from the top thus we need to use a 
# bottom up approach
# global: count # of univalue subtrees
# local: is the subtree rooted at me unival or not?
# So global ans = sum(local answers that are univalue)
#                   root
#                /        \
#               /          \
#              /            \
#         univalleft   right unival
#            / \              \ 
#           5   5              5
#  above even if the left and right tree are unival they to be same as root value

class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


class Solution:
    def unival_subtree(self, root):
        if root is None:
            return 0
        
        global global_count
        global_count = 0

        def helper(node):
            # base case: Leaf node
            if node.left is None and node.right is None:
                global global_count
                # every leaf node is a univalue tree by itself
                global_count += 1
                return True
            
            # recursive case
            am_i_unival = True
            if node.left is not None:
                left_tree = helper(node.left)
                # Here we need to check two conditions to provide the tree is unival
                # 1) wether the left tree is unival
                # 2) check if the node val of the left tree is equal to the root node value
                if left_tree is False or node.val != node.left.val:
                    am_i_unival = False
                    # we do not return here to ensure that the right side of the tree is also evaluated 
                    # to ensure the subtree univals on the right side are not missed
            
            if node.right is not None:
                right_tree = helper(node.right)
                # same 2 checks for the right side as the left
                if right_tree is False or node.val != node.right.val:
                    am_i_unival = False
            
            if am_i_unival:
                global_count += 1
            
            return am_i_unival
        
        helper(root)

        return global_count


#driver program for the above function
# #left side of the tree
root = TreeNode(5)
root.left = TreeNode(1)
root.left.left = TreeNode(5)
root.left.right = TreeNode(5)
#right side of the tree
root.right = TreeNode(5)
root.right.right = TreeNode(5)


# Create a object for the class
obj = Solution()
#now call the class methos with the needed arguments

print(obj.unival_subtree(root))
