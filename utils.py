alpha = 'ABCDEFGHI'

def alpha_range(size):
    return [alpha[i] for i in range(size)]

class UnsolvableException(Exception):
    pass

class BoardException(Exception):
    pass
