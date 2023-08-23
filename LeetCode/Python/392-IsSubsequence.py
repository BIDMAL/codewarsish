"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing
the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        idx = 0
        for char in t:
            if char == s[idx]:
                idx += 1
                if idx == len(s):
                    return True

        return False


def test(input1, input2, output):
    solution = Solution()
    out = solution.isSubsequence(input1, input2)
    assert out == output


if __name__ == '__main__':

    test(
        input1="abc",
        input2="ahbgdc",
        output=True
    )

    test(
        input1="axc",
        input2="ahbgdc",
        output=False
    )

    test(
        input1="",
        input2="ahbgdc",
        output=True
    )
