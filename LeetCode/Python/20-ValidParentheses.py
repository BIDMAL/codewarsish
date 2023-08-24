"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    3. Every close bracket has a corresponding open bracket of the same type.

"""


class Solution:
    def isValid(self, s: str) -> bool:
        openpar = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        stack = []
        for char in s:
            if char in openpar:
                stack.append(char)
            elif len(stack) == 0 or openpar[stack.pop()] != char:
                return False

        return len(stack) == 0


def test(input, output):
    solution = Solution()
    out = solution.isValid(input)
    assert out == output


if __name__ == '__main__':

    test(
        input="()",
        output=True
    )

    test(
        input="()[]{}",
        output=True
    )

    test(
        input="(]",
        output=False
    )
