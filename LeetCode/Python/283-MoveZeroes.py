from typing import List
"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            if nums[slow] != 0:
                slow += 1


def test(*args, expected):
    solution = Solution()
    solution.moveZeroes(*args)
    assert args[0] == expected


if __name__ == '__main__':

    test(
        [0, 1, 0, 3, 12],
        expected=[1, 3, 12, 0, 0]
    )

    test(
        [0],
        expected=[0]
    )

    test(
        [0, 0, 1],
        expected=[1, 0, 0]
    )

    test(
        [0, 1, 0],
        expected=[1, 0, 0]
    )
