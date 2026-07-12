class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = "".join(filter(str.isalnum, s))
        res2 = res.lower()
        left = 0
        right = len(res) - 1
        while left<right:
            if res2[left]!=res2[right]:
                return False
            left+=1
            right-=1
        return True
