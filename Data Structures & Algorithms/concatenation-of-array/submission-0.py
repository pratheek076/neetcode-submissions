class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n)

        for j in range(n):
            ans[j] = nums[j]
            ans[j + n] = nums[j]

        return ans
  



        