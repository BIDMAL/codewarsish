from typing import List
"""
There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes.
The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points
i and i + 1 for all (0 <= i < n). Return the highest altitude of a point.
"""


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = 0
        max_alt = 0
        for d in gain:
            alt += d
            max_alt = max(max_alt, alt)
        return max_alt


def test(*args, expected):
    solution = Solution()
    output = solution.largestAltitude(*args)
    assert output == expected


if __name__ == '__main__':

    test(
        [-5, 1, 5, 0, -7],
        expected=1
    )

    test(
        [-4, -3, -2, -1, 4, 3, 2],
        expected=0
    )
