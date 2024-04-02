import copy
a = [[1, 2, 3],[4 ,5 ,6]]
b = [[1, 2, 3],[4 ,5 ,6]]
c = copy.deepcopy(a)
b [0][1] = 10
c [1][1] = 12

print(a)
print(b)
print(c)

