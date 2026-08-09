class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write = 0
        explore = 0
        counter = 0
        while explore < len(nums):
            if nums[explore] == val:
                counter +=1
                
            else:
                nums[write] = nums[explore]
                write +=1
            
            explore +=1
        return write