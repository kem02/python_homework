import logging

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))


def logger_decorator(func):
    def wrapper(*args, **kwargs):
        # 1. Prepare text for positional and keyword arguments
        if args:
            pos_text = list(args)
        else:
            pos_text = "none"

        if kwargs:
            kw_text = dict(kwargs)
        else:
            kw_text = "none"

        # 2. Call the original function and capture its return value
        result = func(*args, **kwargs)

        # 3. Build a single log string
        log_message = (
            f"function: {func.__name__} "
            f"positional parameters: {pos_text} "
            f"keyword parameters: {kw_text} "
            f"return: {result}"
        )

        # 4. Write that string to decorator.log
        logger.log(logging.INFO, log_message)

        # 5. Give back whatever the function returned
        return result

    return wrapper


@logger_decorator
def say_hello():
    print("Hello, World!")


@logger_decorator
def accept_any_args(*args):
    return True


@logger_decorator
def return_decorator(**kwargs):
    return logger_decorator


say_hello()

# 2) Call the varargs (positional‐only) function with different argument sets:
accept_any_args()  # no arguments
accept_any_args(5)  # one positional argument
accept_any_args("apple", 42, [1, 2])  # three positional arguments

# 3) Call the keyword‐only function with and without keywords:
return_decorator()  # no keyword arguments
return_decorator(alpha=1, beta="B")  # two keyword arguments
