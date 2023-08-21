from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur: int = None
        for idx in range(len(nums) - 1, -1, -1):
            if nums[idx] == cur:
                del (nums[idx])
            else:
                cur = nums[idx]
        return len(nums)


def test(nums: List[int], output, result):
    solution = Solution()
    res = solution.removeDuplicates(nums)
    assert res == output
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
