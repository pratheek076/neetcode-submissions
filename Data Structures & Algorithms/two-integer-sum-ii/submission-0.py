class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first = 0
        second = first + 1
        res = []
        while first != len(numbers) - 1:
            while second < len(numbers):
                sum = numbers[first] + numbers[second]
                if sum == target:
                    res.append(first+1)
                    res.append(second+1)
                    break
                else:
                    second+=1
            first+=1
            second=first+1

        return res
        