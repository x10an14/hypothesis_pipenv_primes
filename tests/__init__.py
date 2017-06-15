from os import path as op


file_dir = op.dirname(__file__)
with open(op.join(file_dir, "primes1.txt")) as f:
    FIRST_MILLION_PRIMES = [int(x) for x in f.read().split(",")]


PRIMES_UNDER_100 = [
    2, 3, 5, 7,
    11, 13, 17, 19, 23, 29,
    31, 37, 41, 43, 47, 53,
    59, 61, 67, 71, 73, 79,
    83, 89, 97, 101]
