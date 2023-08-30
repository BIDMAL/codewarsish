from typing import Optional
"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def of(Cls, lst):
        head = None
        for val in reversed(lst):
            head = Cls(val, head)
        return head

    def __iter__(self):
        head = self
        while head:
            yield head.val
            head = head.next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev


def test(*args, expected):
    solution = Solution()
    head = ListNode.of(*args)
    output = solution.reverseList(head)
    if output:
        output = list(output)
    else:
        output = []

    assert output == expected


if __name__ == '__main__':

    test(
        [1, 2, 3, 4, 5],
        expected=[5, 4, 3, 2, 1]
    )

    test(
        [1, 2],
        expected=[2, 1]
    )

    test(
        [],
        expected=[]
    )
