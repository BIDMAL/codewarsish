from typing import List
from collections import Counter
"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cntr = Counter(nums)
        return cntr.most_common(1)[0][0]

    def majorityElementAlternate(self, nums: List[int]) -> int:
        """
        Moore's Voting Algorithm
        """
        count = 0
        candidate = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate


def test(nums: List[int], output):
    solution = Solution()
    out = solution.majorityElement(nums)
    assert out == output


if __name__ == '__main__':

    test(
        nums=[3, 2, 3],
        output=3
    )

    test(
        nums=[2, 2, 1, 1, 1, 2, 2],
        output=2
    )
