class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k >= len(nums):
            k = k%len(nums)    
        tail = nums[len(nums)-k:len(nums)]
        for i in range(k):
            nums.pop(len(nums)-1)
        nums[:] = tail + nums
        