"""
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

"""


class Solution:
    def tribonacci(self, n: int) -> int:
        res = dict()
        res[0], res[1], res[2] = 0, 1, 1
        for i in range(3, n+1):
            res[i] = res[i-1] + res[i-2] + res[i-3]
        return res[n]


def test(*args, expected):
    solution = Solution()
    output = solution.tribonacci(*args)
    assert output == expected


if __name__ == '__main__':

    test(
        4,
        expected=4
    )

    test(
        25,
        expected=1389537
    )
