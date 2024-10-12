# ens={1,2,3}
# my_set=set(["hello"])
myset=set()
myset.add(1)
myset.add(2)
myset.add(3)

myset.remove(3)
myset.discard(4) #=> efface l'element s'il existe et dans le cas contraire pas d'erreur
# print(myset)

# union, intersection, etc
odds={1,3,5,7,9}
evens={0,2,4,6,8}
primes={2,3,5,7}

u=odds.union(evens)
print(u)

i=odds.intersection(primes)
print(i)

d=odds.difference(primes)
print(d)

s=odds.symmetric_difference(primes)
print(s)

print(odds.issubset(primes))

a=frozenset([1,2,3,4]) #une fois ajouter, on ne peut modifier ni supprimer
print(a)