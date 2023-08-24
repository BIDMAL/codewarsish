from itertools import zip_longest
"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1.
If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1, l2 = len(word1), len(word2)
        res = ''
        for i in range(min(l1, l2)):
            res += word1[i] + word2[i]
        if l1 > l2:
            res += word1[l2:]
        elif l2 > l1:
            res += word2[l1:]
        return res

    def mergeAlternatelyZIP(self, word1: str, word2: str) -> str:
        # using itertools.zip_longest
        return ''.join(a+b for a, b in zip_longest(word1, word2, fillvalue=''))


def test(*args, expected):
    solution = Solution()
    output = solution.mergeAlternately(*args)
    assert output == expected


if __name__ == '__main__':

    test(
        "abc",
        "pqr",
        expected="apbqcr"
    )

    test(
        "ab",
        "pqrs",
        expected="apbqrs"
    )

    test(
        "abcd",
        "pq",
        expected="apbqcd"
    )
