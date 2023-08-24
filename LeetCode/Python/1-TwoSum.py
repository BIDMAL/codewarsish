from typing import List
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # two pointers
        begin, end = 0, len(nums) - 1
        idxd_nums = [(idx, num) for idx, num in enumerate(nums)]
        idxd_nums.sort(key=lambda x: x[1])
        while begin < end:
            curr = idxd_nums[begin][1] + idxd_nums[end][1]
            if curr == target:
                return [idxd_nums[begin][0], idxd_nums[end][0]]
            elif curr > target:
                end -= 1
            else:
                begin += 1
        return []

    def twoSumHM(self, nums: List[int], target: int) -> List[int]:
        # hash map
        numMap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in numMap:
                return [numMap[complement], i]
            numMap[num] = i

        return []


def test(*args, expected):
    solution = Solution()
    output = solution.twoSum(*args)
    assert output == expected


if __name__ == '__main__':

    test(
        [2, 7, 11, 15],
        9,
        expected=[0, 1]
    )

    test(
        [3, 2, 4],
        6,
        expected=[1, 2]
    )

    test(
        [3, 3],
        6,
        expected=[0, 1]
    )
