# Task: https://cs50.harvard.edu/python/psets/8/jar/

class Jar:

    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative int")

        self._capacity = capacity
        self._size = 0


    def __str__(self):
        return "🍪" * self._size


    def deposit(self, n):
        self._check_count(n)

        if self._size + n > self._capacity:
            raise ValueError("Too many cookies")

        self._size += n


    def withdraw(self, n):
        self._check_count(n)

        if n > self._size:
            raise ValueError("Not enough cookies")

        self._size -= n


    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @staticmethod
    def _check_count(n):
        if not isinstance(n, int) or isinstance(n, bool) or n < 0:
            raise ValueError("Number of cookies must be a non-negative int")
