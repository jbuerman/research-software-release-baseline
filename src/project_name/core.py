"""
Core module with a simple example function.
"""

from typing import Optional

def increase(a: int, b: Optional[int] = None) -> int:
    """
    Add one or a specified number to an integer.

    :param a: The number.
    :type a: int
    :param b: Optional addend.
    :type b: Optional[int]
    :return: Either ``a + 1`` if b is None or ``a + b``.
    :rtype: int
    :raises TypeError: If inputs are not integers.
    :raises ValueError: If input b is non-positive.
    """
    if b is None:
        b = 1
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Inputs must be integers")
    if b <= 0:
        raise ValueError("Optional addend must be positive")
    return a + b
