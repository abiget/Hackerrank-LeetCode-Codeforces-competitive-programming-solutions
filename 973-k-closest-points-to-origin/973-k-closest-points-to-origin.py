import math
import numpy as np
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [math.sqrt(points[i][0]**2 + points[i][1]**2) for i in range(len(points))]
        index = np.argsort(distances)
        return np.array(points)[index][:k]
            