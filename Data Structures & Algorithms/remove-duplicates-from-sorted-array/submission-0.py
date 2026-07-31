class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        first = 0
        flag = False
        second = 1
        while second < len(nums):
            if nums[first]!=nums[second]:
                if flag:
                    first+=1
                    nums[first] = nums[second]
                else:
                    first+=1
                
                
            else:
                flag = True

            second+=1
        return first + 1