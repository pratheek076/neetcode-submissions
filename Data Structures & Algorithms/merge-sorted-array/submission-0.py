class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for num in nums2:
            nums1[m] = num
            m+=1
        print(nums1)
        nums1.sort()