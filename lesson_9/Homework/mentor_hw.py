class UnexpectedTypeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


def expected(expecting_types):
    def decorator(func):
        def wrapper_validate(*args, **kwargs):
            func_type = type(func(*args, **kwargs))
            if func_type in expecting_types:
                print(func)
                return func

            print(f"{UnexpectedTypeException}:Was expecting types: str, int")
            return UnexpectedTypeException

        return wrapper_validate

    return decorator


@expected(expecting_types=(str, int))
def func(value):
    print(value)
    return func

