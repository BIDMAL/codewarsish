from typing import List
"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        nlen = len(needle)
        hlen = len(haystack)
        ans = -1
        for idx in range(hlen-nlen+1):
            if haystack[idx:nlen+idx] == needle:
                return idx
        return ans


def test(input1: str, input2: str, output):
    solution = Solution()
    out = solution.strStr(input1, input2)
    assert out == output


if __name__ == '__main__':

    test(
        input1="a",
        input2="a",
        output=0
    )

    test(
        input1="sadbutsad",
        input2="sad",
        output=0
    )

    test(
        input1="leetcode",
        input2="leeto",
        output=-1
    )
