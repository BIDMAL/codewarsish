from typing import List
"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for idx in range(1, len(strs)):
            if prefix == '':
                break
            word = strs[idx]

            if len(prefix) > len(word):
                prefix = prefix[:len(word)]
            length = len(prefix)

            for i in range(length):
                if word[:length-i] == prefix:
                    break
                prefix = prefix[:-1]

        return prefix


def test(input: List[int], output):
    solution = Solution()
    out = solution.longestCommonPrefix(input)
    assert out == output


if __name__ == '__main__':

    test(
        input=["flower", "flow", "flight"],
        output="fl"
    )

    test(
        input=["dog", "racecar", "car"],
        output=""
    )

    test(
        input=["abab", "abab", "abab"],
        output="abab"
    )
