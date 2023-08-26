from typing import List
"""
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies
the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is True if, after giving the ith kid all the extraCandies, they will
have the greatest number of candies among all the kids, or False otherwise.

Note that multiple kids can have the greatest number of candies.
"""


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)

        return [x + extraCandies >= max_candies for x in candies]


def test(*args, expected):
    solution = Solution()
    output = solution.kidsWithCandies(*args)
    assert output == expected


if __name__ == '__main__':

    test(
        [2, 3, 5, 1, 3],
        3,
        expected=[True, True, True, False, True]
    )

    test(
        [4, 2, 1, 1, 2],
        1,
        expected=[True, False, False, False, False]
    )

    test(
        [12, 1, 12],
        10,
        expected=[True, False, True]
    )
