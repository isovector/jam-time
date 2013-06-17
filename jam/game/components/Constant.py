import jam.common.Composable

def Constant(c):
    @jam.common.Composable.c
    def f(x, **kwargs):
        return c
    return f