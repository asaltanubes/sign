from math import copysign
suported_types = [int, float]

def sign(x):
    if type(x) not in suported_types:
        raise TypeError(f'{type(x)} not suported')

    return copysign(1, x)
