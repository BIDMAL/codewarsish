from typing import List
"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

    Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. 
    The remaining elements of nums are not important as well as the size of nums.
    Return k.

"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur: int = None
        for idx in range(len(nums) - 1, -1, -1):
            if nums[idx] == cur:
                del (nums[idx])
            else:
                cur = nums[idx]
        return len(nums)


def test(nums, output, result):
    solution = Solution()
    out = solution.removeDuplicates(nums)
    assert out == output
    assert nums == result


if __name__ == '__main__':

    test(
        nums=[1, 1, 2],
        output=2,
        result=[1, 2]
    )

    test(
        nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
        output=5,
        result=[0, 1, 2, 3, 4]
    )
