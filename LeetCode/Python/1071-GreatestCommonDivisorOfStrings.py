from math import gcd
"""
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
"""


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        return str1[:gcd(len(str1), len(str2))]

    def gcdOfStringsOld(self, str1: str, str2: str) -> str:
        # my first variation... could it be fater tho?
        n = min(len(str1), len(str2))
        while n > 0:
            if len(str1) % n or len(str2) % n:
                n -= 1
                continue
            cd = str1[:n]
            for j in range(n, len(str1), n):
                if str1[j:j+n] != cd:
                    break
            else:
                for j in range(0, len(str2), n):
                    if str2[j:j+n] != cd:
                        break
                else:
                    return cd
            n -= 1
        return ''


def test(*args, expected):
    solution = Solution()
    output = solution.gcdOfStrings(*args)
    assert output == expected


if __name__ == '__main__':

    test(
        "ABCABC",
        "ABC",
        expected="ABC"
    )

    test(
        "ABABAB",
        "ABAB",
        expected="AB"
    )

    test(
        "LEET",
        "CODE",
        expected=""
    )

    test(
        "AAAAAAAAA",
        "AAACCC",
        expected=""
    )
