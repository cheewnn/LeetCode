class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict_Nums = dict()
        lenNums = len(nums)
        for num in nums:
            if dict_Nums.get(num):
                dict_Nums[num] += 1
            else:
                dict_Nums[num] = 1
            if dict_Nums[num] > lenNums/2:
                return num
            
