from typing import Optional
"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverseTree(self, root: TreeNode):
        queue = [root]
        if not root:
            return None
        vals = [root.val]
        while queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
                vals.append(node.left.val)
            else:
                vals.append(None)
            if node.right:
                queue.append(node.right)
                vals.append(node.right.val)
            else:
                vals.append(None)

        return vals

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.traverseTree(p) == self.traverseTree(q)

# TODO: Implement tree builder for tests

# def test(input1, input2, output):
#     solution = Solution()
#     out = solution.isSameTree(input1, input2)
#     assert out == output


# if __name__ == '__main__':

#     test(
#         input1=[1, 2, 3],
#         input2=[1, 2, 3],
#         output=True
#     )

#     test(
#         input1=[1, 2],
#         input2=[1, None, 2],
#         output=False
#     )

#     test(
#         input1=[1, 2, 1],
#         input2=[1, 1, 2],
#         output=False
#     )
