class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
         res = []
         left1, left2 = 0,0
         w1 = len(word1) - 1
         w2 = len(word2) - 1
         while left1 <= w1 or left2 <= w2:
            if left1 <= w1:
                res.append(word1[left1])
                left1+=1
            if left2 <= w2:
                res.append(word2[left2])
                left2+=1
         return "".join(res)

