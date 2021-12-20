class Solution:
    def merge(nums1: [int], m: int, nums2: [int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        while 0 in nums1:
            nums1.remove(0)
        nums1 = nums1[:m]
        nums1 += nums2
        nums1.sort()


if __name__ == '__main__':
    Solution.merge([1,2,3,0,0,0],3,[2,5,6],3)