my_dict={"name":"Max","age":28,"city":"New York","email":"xyz@gmail.com"}

my_dict1={"name":"T-Bag","age":48,"city":"New Jersey","phone":"+243 765 789 987"}
# print(my_dict["age"])

# del my_dict["city"]
# print(my_dict)

# my_dict.pop("name")
# print(my_dict)

# my_dict.popitem()
# print(my_dict)

# for key, value in my_dict.items():
    # print(f"{key}: {value}")


#copier un dictionnaire (meilleure facon)
my_dict_cpy=my_dict.copy()
#OU
new_dict=dict(my_dict)

my_dict.update(my_dict1)
print(my_dict)