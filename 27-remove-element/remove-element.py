class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        lstCount = len(nums)
        for i in range(lstCount):
            if nums[idx] != val:
                idx += 1
            else:
                nums.pop(idx)
        k = len(nums)
        return k

        