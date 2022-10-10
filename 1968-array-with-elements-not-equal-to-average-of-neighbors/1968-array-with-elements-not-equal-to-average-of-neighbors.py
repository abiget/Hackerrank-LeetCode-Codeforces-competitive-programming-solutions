class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        for i in range(1, len(sorted_nums), 2):
            sorted_nums[i], sorted_nums[i-1] = sorted_nums[i-1], sorted_nums[i]
        return sorted_nums
            
        