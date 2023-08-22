from typing import List
"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


def test(input: List[int], output):
    solution = Solution()
    out = solution.lengthOfLastWord(input)
    assert out == output


if __name__ == '__main__':

    test(
        input="Hello World",
        output=5
    )

    test(
        input="   fly me   to   the moon  ",
        output=4
    )

    test(
        input="luffy is still joyboy",
        output=6
    )
