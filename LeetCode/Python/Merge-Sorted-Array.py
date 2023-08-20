from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        pass

if __name__ == '__main__':
    solution = Solution()

    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    res = [1,2,2,3,5,6]

    solution.merge(nums1, m, nums2, n)
    assert nums1 == res