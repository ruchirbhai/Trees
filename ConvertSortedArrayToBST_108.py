# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of 
# the two subtrees of every node never differ by more than 1.
# Example:
# Given the sorted array: [-10,-3,0,5,9],
# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
#       0
#      / \
#    -3   9
#    /   /
#  -10  5

# Definition for a binary tree node.

nums = [-10,-3,0,5,9]

class TreeNode:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class Solution:
    def create_bst(self, nums):
        # we use the lazy manager approrach and write the helper function
        return self.create_bst_helper(nums, 0, len(nums)-1)
    
    def create_bst_helper(self, nums, start, end):
        # Base case: here there are 2 cases len 0 and 1
        if start > end:
            return
        # when len is 1 create a node
        if start == end:
            return TreeNode(nums[start])
        
        # recursive case
        # calculalte the mid point and then pass it to the left and right sides
        mid = start + (end-start)//2    # to avoid overflow we use (end-start)//2  instead of (start+end)/2 explore further
        # based on the mid create the root node
        root_node = TreeNode(nums[mid])

        # call the left side
        root_node.left = self.create_bst_helper(nums, start, mid-1)
        # right side
        root_node.right = self.create_bst_helper(nums, mid+1, end)

        return root_node
    
    def print_bst(self, root):
        
        global count
        count = [10]
        def print_helper(root,space):
            if root is None:
                return
            global count
            space += count[0]

            print_helper(root.right, space)
            print()

            for i in range(count[0], space):
                print(end=" ")
            print(root.data)

            print_helper(root.left, space)
        # give the starting space as 0
        print_helper(root,0)


obj = Solution()        
bst_tree = obj.create_bst(nums)
# print the created tree
obj.print_bst(bst_tree)
