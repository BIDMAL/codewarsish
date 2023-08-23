from functools import reduce
from typing import List
"""
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.
"""


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        begin = 0
        end = len(nums) - 1
        while begin < end:
            mid = (begin + end) // 2
            if nums[mid] == target:
                return True

            if nums[mid] == nums[end]:
                end -= 1
            elif nums[mid] > nums[end]:
                if nums[begin] < target and target < nums[mid]:
                    end = mid - 1
                else:
                    begin = mid + 1
            else:
                if nums[mid] < target and target <= nums[end]:
                    begin = mid + 1
                else:
                    end = mid - 1

        return False


def test(input1, input2, output):
    solution = Solution()
    out = solution.search(input1, input2)
    assert out == output


if __name__ == '__main__':

    test(
        input1=[2, 5, 6, 0, 0, 1, 2],
        input2=0,
        output=True
    )

    test(
        input1=[2, 5, 6, 0, 0, 1, 2],
        input2=3,
        output=False
    )

    test(
        input1=[2, 5, 6, 0, 0, 1, 2],
        input2=3,
        output=False
    )
