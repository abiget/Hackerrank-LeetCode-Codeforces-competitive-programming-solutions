#Domino piling
input_size = [int(i) for i in input().strip().split()]
a, b = input_size[0], input_size[1]

if (a*b) % 2 == 0:
    print(int((a*b)/2))
else:
    print(int((a*b-1)/2))
