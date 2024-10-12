s="""
    bonjour \
    les amis tout va bien ??
"""

char='hello world'
# print(char[1:5])
# print(char[::3])

# pour renverser
# print(char[::-1])

# n=0
# for i in char:
#     if i =="l" or i=="L":
#         n+=1

# print(char.strip())   supprimer les espaces vides dans un string

# print(char.upper())   majuscules
# print(char.lower())   miniscules
# print(char.count('l'))  compter les 'l'

# print(char.replace('world','Universe'))  remplacer une caractere par une autre

# convertir une chaine de caractere en liste
mylist=char.split()
# print(mylist) 
# covertir une liste en chaine de caractere

newstring=' '.join(mylist)
# print(newstring)
cmpt=dict()
for i in char:
    cmpt[i]=char.count(i)
print(cmpt)
    




