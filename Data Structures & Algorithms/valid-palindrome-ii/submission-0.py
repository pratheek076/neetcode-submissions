class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left< right:
            if s[left]!=s[right]:
                v = self.check(left+1, right, s) or self.check(left,right-1, s)
                return v
            left+=1
            right-=1



        return True

    def check(self,left,right, s) -> bool:
        while left<right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True

