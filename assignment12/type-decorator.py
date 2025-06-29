def type_converter(type_of_output):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # 1) Call the original function and save its return value in x
            x = func(*args, **kwargs)
            # 2) Convert x to the requested type, then return that
            return type_of_output(x)

        return wrapper

    return decorator


@type_converter(str)
def return_int():
    return 5


@type_converter(int)
def return_string():
    return "not a number"


y = return_int()
print(type(y).__name__)  # This should print "str"

try:
    y = return_string()
    print("shouldn't get here!")
except ValueError:
    print("can't convert that string to an integer!")  # This is what should happen
