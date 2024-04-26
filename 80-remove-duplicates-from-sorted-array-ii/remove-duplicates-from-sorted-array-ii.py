class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        dict_Existing = dict()
        lenNums = len(nums)
        for i in range(lenNums):
            currNum = nums[idx]
            if dict_Existing.get(currNum):
                if dict_Existing[currNum]==2:
                    nums.pop(idx)
                else:
                    dict_Existing[currNum] += 1
                    idx+=1
            else:
                dict_Existing[currNum] = 1
                idx +=1
        return len(nums)