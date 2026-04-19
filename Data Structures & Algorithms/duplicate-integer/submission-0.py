class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        duplicate_container = set()

        for num in nums:

            if num in duplicate_container:
                return True
            
            duplicate_container.add(num)

        return False        