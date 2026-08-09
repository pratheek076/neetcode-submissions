class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = len(nums) // 2
        res = {}
        for i in range(len(nums)):
            if nums[i] in res:
                res[nums[i]] = res[nums[i]] + 1
            else:
                res[nums[i]] = 1
        
        print(res)
        max_val = 0
        key1 = None
        for key, value in res.items():
            if value > max_val:
                max_val = value
                key1 = key
        
        return key1


         




        