from typing import List
"""
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

    answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
    answer[1] is a list of all distinct integers in nums2 which are not present in nums1.

Note that the integers in the lists may be returned in any order.
"""


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1, s2 = set(nums1), set(nums2)
        return [list(s1-s2), list(s2-s1)]


def test(*args, expected):
    solution = Solution()
    output = solution.findDifference(*args)
    assert output == expected


if __name__ == '__main__':

    test(
        [1, 2, 3],
        [2, 4, 6],
        expected=[[1, 3], [4, 6]]
    )

    test(
        [1, 2, 3, 3],
        [1, 1, 2, 2],
        expected=[[3], []]
    )
