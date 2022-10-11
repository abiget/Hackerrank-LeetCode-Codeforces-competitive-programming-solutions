import math
inputs_list = (map(float, input().strip().split()))
m, n, a = inputs_list
print(math.ceil(m/a)*math.ceil(n/a))
