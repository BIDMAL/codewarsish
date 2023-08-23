from typing import List
"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = [char for char in s.lower() if char.isalnum()]
        return chars == chars[::-1]


def test(input, output):
    solution = Solution()
    out = solution.isPalindrome(input)
    assert out == output


if __name__ == '__main__':

    test(
        input="A man, a plan, a canal: Panama",
        output=True
    )

    test(
        input="race a car",
        output=False
    )

    test(
        input=" ",
        output=True
    )
