#!/usr/bin/env python3
"""
    a type-annotated function make_multiplier that takes a float multiplier
    as argument and returns a function that multiplies a float by multiplier.
"""

from typing import Callable, Iterator, Union, Optional, List, Tuple


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        returns a function that multiplies a float by multiplier.
    """
    def f(n: float) -> float:
        """
            It multiplies a float by multiplier
        """
        return float(n * multiplier)

    return f
