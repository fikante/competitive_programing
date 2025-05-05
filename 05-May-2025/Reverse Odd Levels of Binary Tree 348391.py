# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        queue = deque([root])
        level = 0
        
        while queue:
            size = len(queue)
            if level % 2 == 1:
                # Reverse the values at current level
                left, right = 0, size - 1
                while left < right:
                    queue[left].val, queue[right].val = queue[right].val, queue[left].val
                    left += 1
                    right -= 1
            
            # Process next level
            for _ in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            level += 1
        
        return root
        