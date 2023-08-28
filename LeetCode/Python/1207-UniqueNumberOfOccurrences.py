from collections import Counter
from typing import List
"""
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
"""


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cntr = Counter(arr)
        return len(set(cntr.values())) == len(cntr)

    def uniqueOccurrencesOL(self, arr: List[int]) -> bool:
        # oneliner version
        return (lambda x: len(x) == len(set(x)))(Counter(arr).values())


def test(*args, expected):
    solution = Solution()
    output = solution.uniqueOccurrences(*args)
    assert output == expected


if __name__ == '__main__':

    test(
        [1, 2, 2, 1, 1, 3],
        expected=True
    )

    test(
        [1, 2],
        expected=False
    )

    test(
        [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0],
        expected=True
    )
