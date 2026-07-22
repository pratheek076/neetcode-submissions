class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = {}
        list1 = []
        for s in range(len(strs)):
            signature = "".join(sorted(strs[s]))
            if signature not in maps:
                maps[signature] = []
            maps[signature].append(strs[s])
        
        for val in maps.values():
            list1.append(val)
            
        return list1
            