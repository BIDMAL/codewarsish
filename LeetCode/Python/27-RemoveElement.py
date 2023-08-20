from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for idx in range(len(nums)-1, -1, -1):
            if nums[idx] == val:
                del (nums[idx])

        return len(nums)


def test(nums: List[int], val: int, output, result):
    solution = Solution()
    res = solution.removeElement(nums, val)
    assert res == output
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
