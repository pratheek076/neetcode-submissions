class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for i in range(len(strs[0])):
            char = strs[0][i]
            seen = set()
          
            for x in strs[1:]:
                if i>=len(x) or char != x[i]:
                    return prefix
            prefix+=char
        
            
        return prefix

            


        