class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference = defaultdict(int)
        index = 0
        while index < len(nums):
            i = nums[ index ]
            diff = target - i
            if diff in difference:
                return [ difference[diff], index ]
            else:
                difference[i] = index
            index+=1
        return False    
            