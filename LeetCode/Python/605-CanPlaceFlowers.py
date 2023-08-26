from typing import List
"""
You have a long flowerbed in which some of the plots are planted, and some are not. However,
flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty,
and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
"""


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count, prev = 0, 0

        for cur in flowerbed:
            if cur == 1:
                if prev == 1:
                    count -= 1  # planted with violation
                prev = 1
            else:
                if prev == 1:
                    prev = 0
                else:
                    count += 1
                    prev = 1

        return count >= n


def test(*args, expected):
    solution = Solution()
    output = solution.canPlaceFlowers(*args)
    assert output == expected


if __name__ == '__main__':

    test(
        [1, 0, 0, 0, 1],
        1,
        expected=True
    )

    test(
        [1, 0, 0, 0, 1],
        2,
        expected=False
    )

    test(
        [1, 0, 0, 0, 0, 1],
        2,
        expected=False
    )
