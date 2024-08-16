class InvalidArgumentError(Exception):
    def __init__(self, arg, msg):
        super().__init__(
            f'The `{arg}` (type `{type(arg)}`) is invalid. {msg}')
