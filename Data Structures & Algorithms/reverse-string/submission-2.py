class Solution:
    def reverseString(self, s: List[str]) -> None:
        stack = []
        i=0
        for it in s:
            stack.append(it)
        while stack:
            s[i] = stack.pop()
            i+=1
        