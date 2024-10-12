# add10 = lambda x: x+10

# # print(add10(5))

# multiply= lambda x,y: x*y

# # print(multiply(10,4))

# points2D=[(1,2),(15,1),(5,-1),(10,4)]
# points2D_sorted=sorted(points2D, key=lambda x: x[1])
# print(points2D_sorted)

# a=[1,2,3,4,5]
# b=[x*2 for x in a]
# print(b)

# a=[1,2,3,4,5]
# b=map(lambda x: x*2, a)
# print(list(b))

# a=[1,2,4,5,6]
# b=filter(lambda x: x%2==0, a)
# # print(list(b))

# c=[x for x in a if x%2==0]
# print(c)
from functools import reduce

a=[1,2,3,4]
b=reduce( lambda x,y: x*y, a)
print(b)
