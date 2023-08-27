"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words.
The returned string should only have a single space separating the words. Do not include any extra spaces.
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split()
        return ' '.join(s_list[::-1])


def test(*args, expected):
    solution = Solution()
    output = solution.reverseWords(*args)
    assert output == expected


if __name__ == '__main__':

    test(
        "the sky is blue",
        expected="blue is sky the"
    )

    test(
        "  hello world  ",
        expected="world hello"
    )

    test(
        "a good   example",
        expected="example good a"
    )
