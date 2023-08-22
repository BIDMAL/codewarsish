from typing import List
"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                max_profit = max(prices[right] - prices[left], max_profit)
            else:
                left = right
            right += 1

        return max_profit


def test(nums: List[int], output):
    solution = Solution()
    out = solution.maxProfit(nums)
    assert out == output


if __name__ == '__main__':

    test(
        nums=[7, 1, 5, 3, 6, 4],
        output=5
    )

    test(
        nums=[7, 6, 4, 3, 1],
        output=0
    )

    test(
        nums=[7, 3, 8, 2, 1],
        output=5
    )

    test(
        nums=[7, 3, 8, 2, 1, 9],
        output=8
    )
