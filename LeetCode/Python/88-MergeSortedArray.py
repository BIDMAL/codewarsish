from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        c1 = m - 1
        c2 = n - 1
        wi = m + n - 1
        while wi >= 0:
            if c2 >= 0 and c1 >= 0:
                if nums1[c1] >= nums2[c2]:
                    nums1[wi] = nums1[c1]
                    c1 -= 1
                else:
                    nums1[wi] = nums2[c2]
                    c2 -= 1
            elif c1 >= 0:
                nums1[wi] = nums1[c1]
                c1 -= 1
            else:
                nums1[wi] = nums2[c2]
                c2 -= 1
            wi -= 1


def test(nums1: List[int], m: int, nums2: List[int], n: int, result):
    solution = Solution()
    solution.merge(nums1, m, nums2, n)
    assert nums1 == result


if __name__ == '__main__':

    test(
        nums1=[1, 2, 3, 0, 0, 0],
        m=3,
        nums2=[2, 5, 6],
        n=3,
        result=[1, 2, 2, 3, 5, 6]
    )

    test(
        nums1=[1],
        m=1,
        nums2=[],
        n=0,
        result=[1]
    )

    test(
        nums1=[0],
        m=0,
        nums2=[1],
        n=1,
        result=[1]
    )

    test(
        nums1=[2, 0],
        m=1,
        nums2=[1],
        n=1,
        result=[1, 2]
    )
