"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        s_list = list(s)
        begin, end = 0, len(s_list) - 1
        while begin < end:
            if s_list[begin] not in vowels:
                begin += 1
                continue
            if s_list[end] not in vowels:
                end -= 1
                continue
            s_list[begin], s_list[end] = s_list[end], s_list[begin]
            begin += 1
            end -= 1
        return ''.join(s_list)


def test(*args, expected):
    solution = Solution()
    output = solution.reverseVowels(*args)
    assert output == expected


if __name__ == '__main__':

    test(
        "hello",
        expected="holle"
    )

    test(
        "leetcode",
        expected="leotcede"
    )

    test(
        "aA",
        expected="Aa"
    )
