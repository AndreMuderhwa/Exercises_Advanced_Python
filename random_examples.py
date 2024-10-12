# import random 
# a = random.randrange(1,10)
# # print(a)
# mylist=list("ABCDEFGHIJKLMN")
# b=random.sample(mylist, 3)
# print(b)

import secrets

a=secrets.randbelow(10)
# print(a)

b=secrets.randbits(4)
# print(b)

mylist=list("ABCDEFGHIJKLMN")
c=secrets.choice(mylist)
# print(c)


#numpy
