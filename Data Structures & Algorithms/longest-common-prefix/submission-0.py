class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for x in strs[1:]:
            while not x.startswith(prefix):
                prefix = prefix[:-1]
        
        return prefix
            





        
    