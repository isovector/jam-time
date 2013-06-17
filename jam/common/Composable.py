# this is deliberately g(f) to implement
# left-associativity of the composition
compose = lambda f, g: lambda *args, **kwargs:\
        g(f(*args, **kwargs), **kwargs)

class c(object):
    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        return self.f(*args, **kwargs)

    def __mul__(self, other):
        return c(compose(self, other))
