mylist=['banana','apple','lemon']
#les index negatifs permettent de recuperer les elements en commencant par le dernier
# print(mylist[-2])

# for i in mylist:
#     print(i)

# if "apple" in mylist:
#     print("yes")
# else:
#     print("no")


#ternary condition
# print("yes") if "apple" in mylist else print("no")

# print(len(mylist))

# mylist.append("orange")
# print(mylist)

# mylist.insert(0, "Blueberry")
# print(mylist)
# item=mylist.pop() #prends le dernier element de la liste
# print(item)
# print(mylist)

# mylist.remove("lemon")
# mylist.clear() #effacer tout
mylist.reverse() #perturber l'ordre
#si la liste contient des nombres on peut utiliser .sort() ou sorted()
#  pour arranger du plus petit au plus grand

n=[0,-1,-9,3,2,7,10,1]
# new_n=sorted(n)
# print(new_n)
# print(mylist)
# print(n *2)
# print(mylist + n)
new_list=[1,2,3,4,5,6,7,8,9]
#print(new_list[::2]) #step

old_list=new_list.copy() #meilleur maniere de copier

squared_list=[i*i for i in new_list]
print(squared_list)
