class UnexpectedTypeException:
    def __init__(self, expecting):
        self.expecting_types = expecting


def expected(expecting_types, str, int):
    def decorator(func):
        def wrapper_validate(*args, **kwargs):
            func_type = type(func(*args, **kwargs))
            expecting_types = str, int
            for i in expecting_types:
                if func_type == i:
                    print(func)

            else:

                print(f"{UnexpectedTypeException}:Was expecting types: str, int")
                return UnexpectedTypeException

        return wrapper_validate

    return decorator


@expected(expecting_types=(str, int))
def func():
    value = input("Please, input any tuple with string  and integer:")
    print(value)
    return value
