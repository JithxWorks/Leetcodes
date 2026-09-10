
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root):
        
        self.ans = 0
        
        def dfs(node):
            if node is None:
                return 0, 0
            
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            
            total_sum = node.val + left_sum + right_sum
            total_count = 1 + left_count + right_count
            
            if node.val == total_sum // total_count:
                self.ans += 1
            
            return total_sum, total_count
        
        dfs(root)
        
        return self.ans

