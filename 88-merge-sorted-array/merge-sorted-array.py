class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ct1 = 0
        ct2 = 0
        ret = []
        complete1 = False
        complete2 = False
        while ct1 < m and ct2 < n:
            if nums1[ct1] <= nums2[ct2]:
                ret.append(nums1[ct1])
                ct1 += 1
            else:
                ret.append(nums2[ct2])
                ct2 += 1
        if ct1 == m:
            complete1 = True
        if ct2 == n:
            complete2 = True
        if not complete2:
            ret += nums2[ct2:n]
        if not complete1:
            ret += nums1[ct1:m]
        nums1[:] = ret
        