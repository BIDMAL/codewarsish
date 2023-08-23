from collections import Counter
"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        chars = Counter(magazine)
        chars.subtract(ransomNote)
        return all([val >= 0 for val in chars.values()])

    # alternative soplution
    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        st1, st2 = Counter(ransomNote), Counter(magazine)
        return st1 & st2 == st1


def test(input1, input2, output):
    solution = Solution()
    out = solution.canConstruct(input1, input2)
    assert out == output


if __name__ == '__main__':

    test(
        input1="a",
        input2="b",
        output=False
    )

    test(
        input1="aa",
        input2="ab",
        output=False
    )

    test(
        input1="aa",
        input2="aab",
        output=True
    )
