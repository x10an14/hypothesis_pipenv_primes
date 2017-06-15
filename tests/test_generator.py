from prime import generator
from . import FIRST_MILLION_PRIMES

from hypothesis import given
from hypothesis import settings
from hypothesis import Verbosity
from hypothesis.strategies import integers as ints

FIRST_MILLION_PRIMES = [int(x) for x in FIRST_MILLION_PRIMES]


@given(
    ints(max_value=int(1e6) - 1)
)
@settings(
    verbosity=Verbosity.verbose,
    timeout=20
)
def test_prime_generator(nth_prime):
    try:
        generated_prime = generator(nth_prime)
        assert generated_prime in FIRST_MILLION_PRIMES
    except TypeError as e:
        if type(nth_prime) is int and nth_prime >= 0:
            raise e
