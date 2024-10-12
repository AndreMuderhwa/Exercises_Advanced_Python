# from itertools import product
# a=[1,2]
# b=[3,4]
# pr=product(a,b)
# print(list(pr))

# from itertools import permutations
# a=[1,2,3]
# perm=permutations(a,2)
# print(list(perm))

# from itertools import combinations, combinations_with_replacement
# a=[1,2,3,4]
# comb=combinations(a,2)
#print(list(comb))

# comb_wr=combinations_with_replacement(a,2)
# print(list(comb_wr))


# from itertools import accumulate
# import operator 
# a=[1,2,3,4]
# acc=accumulate(a, func=operator.add)
# print(list(acc))

# from itertools import groupby
# a=[1,2,3,4]
# group=groupby(a,key=lambda x: x<3)
# for key, value in group:
#     print(key, list(value))

# persons=[{"name":"Daniel","age":25},{"name":"Jack","age":25},
#         {"name":"Glo","age":27},{"name":"Jules","age":28}
#         ]

# grp=groupby(persons, key=lambda y: y['age'])
# for key, value in grp:
#     print(key, list(value))

# from itertools import count, cycle, repeat
# for i in count(10):
#     print(i)
#     if i ==15:
#         break

# a=[1,2,3]
# for i in cycle(a):
#     print(i)
#     if i==3:
#         break

# for i in repeat(1,4):
#     print(i)
#     if i==1:
#         break