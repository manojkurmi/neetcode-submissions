from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = defaultdict(list)
        for i, num in enumerate(nums):
            numMap[num].append(i)

        for i, num in enumerate(nums):
            other = target-num
            if other in numMap:
                if len(numMap[other]) == 1:
                    if i != numMap[other][0]:
                        return [i, numMap[other][0]]
                else:
                    return [i, numMap[other][1]]
        return None

