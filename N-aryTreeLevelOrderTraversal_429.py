# https://leetcode.com/problems/n-ary-tree-level-order-traversal/

# Given an n-ary tree, return the level order traversal of its nodes' values.

# Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

# Example 1:
# Input: root = [1,null,3,2,4,null,5,6]
# Output: [[1],[3,2,4],[5,6]]

# Example 2:
# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]

# Constraints:

# The height of the n-ary tree is less than or equal to 1000
# The total number of nodes is between [0, 10^4]

from collections import deque

global height 
height = 0

class TreeNode:
    def __init__(self, key):
        """
        :data: key
        :children: empty []
        :rtype: None
        """
        self.data = key
        self.children = []
    
    def add_child(self, child):
        self.children.append(TreeNode(child))

class Solution:
    def n_ary_tree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # edge case where the input is empty
        if root is None:
            return

        # create the results list
        result = []

        # copy the given queue
        q = deque([root])

        # while len of q is not zero keep the while loop going
        while len(q) != 0:
            # get the count of all the nodes in this level
            numnodes = len(q)
            # create a tmp list for storing the values of nodes at each level
            tmp = []

            # go through each of the nodes
            for _ in range(numnodes):
                # pop the entire tree from the current root to the node variable
                node = q.popleft()
                # copy the key value only to tmp
                tmp.append(node.data)
                # for each child in the list we append the data
                for child in node.children:
                    q.append(child)            
            result.append(tmp)
        
        return result
    

    def nary_height(self, root):
        if root is None:
            return 0
            
        
        height = 0
        for child in root.children:
            height = max(height, self.nary_height(child))
        
        return height + 1


#driver program for the above function

root = TreeNode(1)
root.add_child(3)
root.add_child(2)
root.add_child(4)

root.children[0].add_child(5)
root.children[0].add_child(6)

# Create a object for the class
obj = Solution()
#now call the class methos with the needed arguments
print(obj.n_ary_tree(root))
print(obj.nary_height(root))