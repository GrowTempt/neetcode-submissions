class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numsDupe = nums
        for num in numsDupe:
            if num == 0:
                nums.append(0)
                nums.remove(num)
