class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 1
        maj = nums[0]
        ptr = 1
        while ptr < len(nums):
            if nums[ptr] == maj:
                counter+=1
            else:
                if counter<0:
                    maj = nums[ptr]
                    counter +=1
                else:
                    counter-=1
            
            ptr += 1
        return maj
        