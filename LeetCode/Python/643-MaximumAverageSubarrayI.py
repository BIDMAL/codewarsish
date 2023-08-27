from typing import List
"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
Any answer with a calculation error less than 10e-5 will be accepted.
"""


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sub = sum(nums[:k])
        max_sub = curr_sub
        idx = k
        while idx < len(nums):
            curr_sub -= nums[idx-k] - nums[idx]
            max_sub = max(max_sub, curr_sub)
            idx += 1

        return max_sub/k


def test(*args, expected):
    solution = Solution()
    output = solution.findMaxAverage(*args)
    assert output == expected


if __name__ == '__main__':

    test(
        [1, 12, -5, -6, 50, 3],
        4,
        expected=12.75000
    )

    test(
        [5],
        1,
        expected=5.00000
    )

    test(
        [0, 1, 1, 3, 3],
        4,
        expected=2.00000
    )

    test(
        [0, 4, 0, 3, 2],
        1,
        expected=4.00000
    )
