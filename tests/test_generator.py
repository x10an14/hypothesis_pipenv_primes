from prime import generator

from hypothesis import given
from hypothesis import reject
from hypothesis.strategies import integers as ints

FIRST_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]


@given(ints(max_value=1))
def test_prime_generator(nth_prime):
    try:
        generated_prime = generator(nth_prime)
    except TypeError as e:
        if not nth_prime < 0:
            raise e
        reject()
    assert generated_prime == FIRST_PRIMES[nth_prime + 1]
