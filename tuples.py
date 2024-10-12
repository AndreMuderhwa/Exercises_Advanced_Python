# my_tuple=("Allen","Koogar",90)
# my_tupl="Allen","Koogar",90
#les deux mannieres de declarer un tuple
# tuple1=("Allen",) # => si le tuple comprends un seul element
# my=tuple(['Allen','Koogar',90,'JR Kala'])
# # print(type(tuple))
# print(my[::2])
# print(my[-1])
# if "allen" in my_tuple:
#     print("yes")
# else:
#     print("No")

# new_tuple=['a','p','p','l','e']
#print(new_tuple.count('p'))
# print(new_tuple.index('l'))

# new_tuple=(1,2,3,4,5,6,7,8,9)
# print(new_tuple[::-1]) #le step negatif permet de perturber l'ordre des elements

# tp=(1,2,3,4,5,6)
# i1, *i2, i3=tp

# print(i1)
# print(i2)
# print(i3)

import sys
my_list=[0,1,2,"hello",True]
my_tuple=(0,1,2,"hello",True)

print(f"{sys.getsizeof(my_list)} bytes for list")
print(f"{sys.getsizeof(my_tuple)} bytes for tuple")
