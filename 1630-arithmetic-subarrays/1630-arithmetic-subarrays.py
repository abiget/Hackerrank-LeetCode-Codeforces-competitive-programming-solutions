class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        is_arithm_list = []
        for i in range(len(l)):
            sub_nums = sorted(nums[l[i]:r[i]+1])
            count = 0
            for j in range(1, len(sub_nums)-1):
                prev = sub_nums[j] - sub_nums[j-1]
                if prev == sub_nums[j+1] - sub_nums[j]:
                    count +=1
                else:
                    break
            if count == len(sub_nums)-2:
                is_arithm_list.append(True)
            else:
                is_arithm_list.append(False)
        return is_arithm_list
                
                
                
            
            