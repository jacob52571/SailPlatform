class InvalidArgumentError(Exception):
    def __init__(self, arg, msg):
        super().__init__(
            f'The `{arg}` (type `{type(arg)}`) is invalid. {msg}')

def validate_positive_number(number):
    if not isinstance(number, float) and not isinstance(number, int):
        raise InvalidArgumentError(number, "Only the following types are allowed: <class 'int'>, <class 'float'>")

    if not (number > 0):
        raise InvalidArgumentError(number, "The argument must be a positive number.")

    return None

def validate_non_empty_string(string):
    if not isinstance(string, str):
        raise InvalidArgumentError(string, "The argument must be a string.")

    if len(string) == 0:
        raise InvalidArgumentError(string, "The argument must be a non-empty string.")

    return None

