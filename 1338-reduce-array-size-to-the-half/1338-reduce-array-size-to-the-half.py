from queue import PriorityQueue
from collections import defaultdict
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        #create frq map
        frq_map = defaultdict(int)
        for item in arr:
            frq_map[item] = frq_map[item]+1
        
        #priority queue
        queue = PriorityQueue()
        for value in frq_map.values():
            queue.put(-value)
        
        count = 0 #least number of elements to remove
        rm_frq_sum = 0
        
        while rm_frq_sum < len(arr)/2:
            count += 1
            value = -queue.get()
            rm_frq_sum += value
        return count
            
        