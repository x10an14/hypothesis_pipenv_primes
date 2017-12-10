from . import FIRST_MILLION_PRIMES
from prime import sieve

from hypothesis import given
from hypothesis import settings
from hypothesis import Verbosity
from hypothesis.strategies import values
from hypothesis.strategies import sampled_from
from hypothesis.strategies import integers as ints


@given(
    ints(max_value=max(FIRST_MILLION_PRIMES)) |
    sampled_from(FIRST_MILLION_PRIMES) |
    values()
)
@settings(
    verbosity=Verbosity.verbose,
    max_examples=1_000,
)
def test_prime_sieve(pot_prime):
    try:
        is_prime = pot_prime in FIRST_MILLION_PRIMES
        assert sieve(pot_prime) is is_prime
    except TypeError as e:
        if type(pot_prime) is int and pot_prime >= 0:
            raise e
