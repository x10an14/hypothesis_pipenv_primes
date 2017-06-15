from itertools import islice
from contextlib import suppress


def generator(nth_prime):
    """
    Prime number generator library function.

    Input: Anything.
    Output (if `nth_prime` can be cast into a positive integer): The generator will yield all
      primes up and including the `nth_prime`.
    Output (if `nth_prime` cannot be cast into a positive integer): int(-1).
    """
    with suppress(TypeError):
        nth_prime = int(nth_prime)
    if not type(nth_prime) is int or nth_prime < 0:
        # raise TypeError("Input needs to be of positive integer type!")
        return -1

    return next(islice(postponed_sieve(), nth_prime, nth_prime + 1))


def sieve(pot_prime):
    """
    Prime number sieve library function.

    Input: Anything
    Output: True if input (can be cast into a positive integer and) prime.
      Otherwise False.
    """
    with suppress(TypeError):
        pot_prime = int(pot_prime)
    if not type(pot_prime) is int or pot_prime < 0:
        raise TypeError("Input needs to be of positive integer type!")

    return prime_check2(pot_prime)


def prime_check1(pot_prime):
    """Function prime_check1 - by x10an14."""
    if pot_prime == 2:
        return True
    elif pot_prime < 2 or pot_prime % 2 == 0:
        return False
    else:
        from math import sqrt
        for num in range(3, int(sqrt(pot_prime) + 1), step=2):
            if pot_prime % num == 0:
                return False
        return True


def prime_check2(pot_prime):
    """
    Function isPrime - by dawg.

    Link: https://stackoverflow.com/a/15285588/1503549
    """
    if pot_prime == 2 or pot_prime == 3:
        return True
    elif pot_prime < 2 or pot_prime % 2 == 0:
        return False
    elif pot_prime < 9:
        return True
    elif pot_prime % 3 == 0:
        return False
    else:
        root = int(pot_prime ** 0.5)
        next_prime = 5
        while next_prime <= root:
            # print('\t', next_prime)
            if pot_prime % next_prime == 0:
                return False
            if pot_prime % (next_prime + 2) == 0:
                return False
            next_prime += 6
        return True


def postponed_sieve():
    """
    Postponed Sieve prime numbers generator - by Will Ness.

    Link: https://stackoverflow.com/a/10733621/1503549
    """
    from itertools import count
    yield 2
    yield 3
    yield 5
    yield 7

    # a separate base Primes Supply:
    ps = postponed_sieve()

    # #                                 For the first iteration:
    p = next(ps) and next(ps)               # (3) a Prime to add to dict
    q = p * p                               # (9) its sQuare

    # Dict to keep/map all found primes/composites
    sieve = {}

    for c in count(9, 2):                   # c == the Candidate
        if c in sieve:                      # c's a multiple of some base prime
            s = sieve.pop(c)                # #   i.e. a composite ; or
        elif c < q:
            yield c                         # a prime
            continue
        else:   # (c==q):                   # or the next base prime's square:
            s = count(q + 2 * p, 2 * p)     # #  (9+6, by 6 : 15,21,27,33,...)
            p = next(ps)                    # #  (5)
            q = p * p                       # #  (25)
        for m in s:                         # the next multiple
            if m not in sieve:              # no duplicates
                break
        sieve[m] = s    # original test entry: ideone.com/WFv4f
