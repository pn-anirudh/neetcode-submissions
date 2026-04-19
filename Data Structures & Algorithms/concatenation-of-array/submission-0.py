class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        res = [0]*(2*n)

        for index,num in enumerate(nums):
            res[index] = res[index+n] = num
        
        return res