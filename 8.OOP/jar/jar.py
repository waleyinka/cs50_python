# Task: https://cs50.harvard.edu/python/psets/8/jar/

class Jar:

    def __init__(self, capacity=12):
        """
        Initializes a new Jar instance with a specified capacity.
        The capacity must be a non-negative integer. The initial size of the jar is set to zero.
        """
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative int")

        self._capacity = capacity
        self._size = 0

    # 
    def __str__(self):
        """
        Returns a string representation of the jar's contents using cookie emojis.
        Each cookie emoji represents one cookie in the jar."""
        return "🍪" * self._size


    def deposit(self, n):
        """
        Adds a specified number of cookies to the jar.
        Raises a ValueError if the number of cookies to add is negative or exceeds the jar's capacity.
        """
        self._check_count(n)

        if self._size + n > self._capacity:
            raise ValueError("Too many cookies")

        self._size += n


    def withdraw(self, n):
        """
        Removes a specified number of cookies from the jar.
        Raises a ValueError if the number of cookies to remove is negative or exceeds the jar's size.
        """
        self._check_count(n)

        if n > self._size:
            raise ValueError("Not enough cookies")

        self._size -= n


    @property
    def capacity(self):
        """
        Returns the capacity of the jar.
        """
        return self._capacity

    @property
    def size(self):
        """
        Returns the current size of the jar.
        """
        return self._size

    @staticmethod
    def _check_count(n):
        """
        Checks if the number of cookies is a non-negative integer.
        Raises a ValueError if the condition is not met.
        """
        if not isinstance(n, int) or isinstance(n, bool) or n < 0:
            raise ValueError("Number of cookies must be a non-negative int")
