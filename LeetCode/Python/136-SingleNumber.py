from functools import reduce
from typing import List
"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        return reduce(lambda a, b: a ^ b, nums)


def test(input, output):
    solution = Solution()
    out = solution.singleNumber(input)
    assert out == output


if __name__ == '__main__':

    test(
        input=[2, 2, 1],
        output=1
    )

    test(
        input=[4, 1, 2, 1, 2],
        output=4
    )

    test(
        input=[1],
        output=1
    )
