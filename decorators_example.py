# # two kinds : functions decorators, class decorators
# # les decorateurs permettent d'etendre les fonctionnalites 
# # d'une fonction sans changer son code
# import functools 

# def start_end_decorator(func):

#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         # print("Sart") do something before
#         rs =func(*args, **kwargs)
#         # print("End") do something after
#         return rs
#     return wrapper


# @start_end_decorator
# def print_name():
#     print('Andrew Decorator')

# @start_end_decorator
# def exposant(x, y):
#     return x**y

# # print(help(exposant(2,3)))
# # print(exposant.__name__)

# # decorators with parameters

# def repeat(num_times):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for _ in range(num_times):
#                 rs =func(*args, **kwargs)
#             return rs
#         return wrapper
#     return decorator

# @repeat(num_times=5)
# def greet(name):
#     print(f"Hello {name}")


# greet('Sanel')

# class Decorators

class CountCalls:
    def __init__(self, func):
        self.func=func
        self.num_calls=0
    def __call__(self, *args, **kwargs):
        self.num_calls +=1
        print(f"This is executed {self.num_calls} times")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print("hello")

say_hello()
say_hello()