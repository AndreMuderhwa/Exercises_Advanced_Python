# x=-5
# if x<0:
#     raise Exception("X should be positive")

# try:
#     a=5/2
#     b=5+'10'
# except Exception as e:
#     print(e)

# except TypeError as e:
#     print(e)

# else:
#     print("Everything is fine")

# finally:
#     print("cool")


class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message=message
        self.value=value

def check_value(value):
    if value >100:
        raise ValueTooHighError("Value is too high")
    if value <5:
        raise ValueTooSmallError("Value is too small", value)
    
try:
    check_value(3)
except ValueTooHighError as e:
    print(e)

except ValueTooSmallError as e:
    print(e.message, e.value)


for _ in range(100):
    print("cool")