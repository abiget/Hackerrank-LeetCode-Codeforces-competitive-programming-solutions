class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        new_list = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if j != i and nums[i] > nums[j]:
                    count += 1
            new_list.append(count)
        return new_list
                
            