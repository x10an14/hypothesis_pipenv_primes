from itertools import islice

from prime import generator

from hypothesis import given
from hypothesis.strategies import integers as ints

MAX_NTH_PRIME = int(5e4)


@given(
    ints(min_value=-MAX_NTH_PRIME, max_value=MAX_NTH_PRIME)
)
def test_prime_generator(nth_prime):
    generated_prime = generator(nth_prime)
    if nth_prime < 0:
        assert generated_prime == -1
    else:
        assert generated_prime == next(
            islice(erat3(), nth_prime, nth_prime + 1))


def erat3():
    """Faster function completely stolen from S/O."""
    from itertools import compress
    from itertools import cycle
    from itertools import count
    D = {9: 3, 25: 5}
    yield 2
    yield 3
    yield 5
    MASK = 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0,
    MODULOS = frozenset((1, 7, 11, 13, 17, 19, 23, 29))

    for q in compress(
        islice(count(7), 0, None, 2),
        cycle(MASK)
    ):
        p = D.pop(q, None)
        if p is None:
            D[q * q] = q
            yield q
        else:
            x = q + 2 * p
            while x in D or (x % 30) not in MODULOS:
                x += 2 * p
            D[x] = p
