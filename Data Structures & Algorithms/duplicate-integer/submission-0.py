class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        for num in nums:
            if num in hashMap:
                return True
            else: # If number is not in hashMap, we add it
                hashMap[num] = 1
        return False