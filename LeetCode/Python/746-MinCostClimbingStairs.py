from typing import List
"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

"""


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        spent = {0: cost[0], 1: cost[1]}
        for i in range(2, len(cost)):
            spent[i] = min(spent[i-1], spent[i-2]) + cost[i]

        return min(spent[len(cost)-1], spent[len(cost)-2])


def test(*args, expected):
    solution = Solution()
    output = solution.minCostClimbingStairs(*args)
    assert output == expected


if __name__ == '__main__':

    test(
        [10, 15, 20],
        expected=15
    )

    test(
        [1, 100, 1, 1, 1, 100, 1, 1, 100, 1],
        expected=6
    )

    test(
        [0, 2, 2, 1],
        expected=2
    )
