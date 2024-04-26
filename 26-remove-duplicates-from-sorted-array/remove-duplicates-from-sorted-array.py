class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
            idx = 0
            ctNums = len(nums)
            dict_Appeared = dict()
            for i in range(ctNums):
                if dict_Appeared.get(nums[idx]) == None:
                    dict_Appeared[nums[idx]] = 0
                    idx += 1
                else:
                    dict_Appeared[nums[idx]] += 1
                    nums.pop(idx)
            k = len(nums)
            return k
        