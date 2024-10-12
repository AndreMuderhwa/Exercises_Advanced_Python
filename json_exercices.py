import json

# person={
#     "firstname":"Andrew",
#     "lastname":"Ghost",
#     "age":28,
#     "city":"Goma",
#     "hasChildren":False,
#     "titles":["engineer","programer"]  
# } 
# # dict to json
# personJSON=json.dumps(person, indent=4, sort_keys=True)
# # print(personJSON)

# # dict to json file
# with open('person.json','w') as file:
#     json.dump(person, file, indent=4)

# # json to dict
# person1=json.loads(personJSON)
# # print(person1)


# # json file to dict

# with open('person.json', 'r') as file:
#     person2=json.load(file)
#     print(person2)

class User:
    def __init__(self, name, age):
        self.name=name
        self.age=age

#1ere facon

# def encode_user(obj):
#     if isinstance(obj, User):
#         return {"name":obj.name, "age":obj.age, obj.__class__.__name__:True}
#     raise TypeError(" Object of type User is not JSON serializable")


# user=User("Sanel",25)

# userJSON=json.dumps(user,default=encode_user)
# print(userJSON)

# 2em facon

user=User("Sanel",25)

from json import JSONEncoder

class UserEncoder(JSONEncoder):
    def default(self,obj):
        if isinstance(obj, User):
            return {"name":obj.name, "age":obj.age, obj.__class__.__name__:True}
        return JSONEncoder.default(self, obj)
    
# from dict to json
userJSON=UserEncoder().encode(user)
# print(userJSON)


# from json to dict 
user1=json.loads(userJSON)
# print(user1)

# from json to Object(class)
def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct

user2=json.loads(userJSON, object_hook=decode_user)
print(type(user2))
print(user2.name)