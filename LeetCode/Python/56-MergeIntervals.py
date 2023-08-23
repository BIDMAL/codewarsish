from typing import List
"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array
of the non-overlapping intervals that cover all the intervals in the input.
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda k: k[0])
        res = []
        curr = intervals[0]
        for interval in intervals[1:]:
            if interval[0] <= curr[1]:
                curr[1] = max(curr[1], interval[1])
            else:
                res.append(curr)
                curr = interval
        res.append(curr)
        return res


def test(input, output):
    solution = Solution()
    out = solution.merge(input)
    assert out == output


if __name__ == '__main__':

    test(
        input=[[1, 3], [2, 6], [8, 10], [15, 18]],
        output=[[1, 6], [8, 10], [15, 18]]
    )

    test(
        input=[[1, 4], [4, 5]],
        output=[[1, 5]]
    )

    test(
        input=[[1, 4], [2, 3]],
        output=[[1, 4]]
    )
