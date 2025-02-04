# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        queue = [(root, 0)]
        output = []

        if not root:
            return output

        while queue:
            node, level = queue.pop(0)

            if len(output) <= level:
                output.append([])
            level_lst = output[level]
            level_lst.append(node.val)

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return list(reversed(output))
