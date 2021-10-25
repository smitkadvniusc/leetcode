#https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        ls = []
        max_h = 1
        ls.append([root,1])
        while(len(ls) != 0):
            temp,h = ls.pop()
            if max_h < h:
                max_h = h
            if temp.left is not None:
                ls.append([temp.left,h+1])
            if temp.right is not None:
                ls.append([temp.right,h+1])
        
        return max_h
            
