def flip(f):
    return lambda a: lambda b: f(b)(a)


def compose(f):
    return lambda g: lambda x: f(g(x))


def identity(x):
    return x


def constant(x):
    return lambda _: x
