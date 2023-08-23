from typing import List
"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed.
Then return the number of elements in nums which are not equal to val.
Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

    Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of
    nums are not important as well as the size of nums.
    Return k.

"""


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for idx in range(len(nums)-1, -1, -1):
            if nums[idx] == val:
                del (nums[idx])

        return len(nums)


def test(nums, val, output, result):
    solution = Solution()
    out = solution.removeElement(nums, val)
    assert out == output
    assert nums == result


if __name__ == '__main__':

    test(
        nums=[3, 2, 2, 3],
        val=3,
        output=2,
        result=[2, 2]
    )

    test(
        nums=[0, 1, 2, 2, 3, 0, 4, 2],
        val=2,
        output=5,
        result=[0, 1, 3, 0, 4]
    )
