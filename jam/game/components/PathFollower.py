import jam.common.Composable

def PathFollower(self):
    @jam.common.Composable.c
    def f(pos, delta = 0, **kwargs):
        return pos + 5 * delta
    return f

pos = PathFollower(None) * PathFollower(None)
print pos(0, delta = 5)