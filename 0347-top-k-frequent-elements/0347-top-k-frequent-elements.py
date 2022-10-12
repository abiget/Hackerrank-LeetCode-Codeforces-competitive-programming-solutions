from collections import defaultdict
import numpy as np

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frq_map = defaultdict(int)
        
        for num in nums:
            frq_map[num] = frq_map[num]+1
            
        index = np.argsort(list(frq_map.values()))
        return list(reversed(np.array(list(frq_map.keys()))[index]))[:k]