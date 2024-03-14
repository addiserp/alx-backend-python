#!/usr/bin/env python3
"""
    Augment the following code with the correct duck-typed annotations:
"""
from typing import Any, Union, Sequence, Iterable, List, Tuple


# input types are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
        first element safe
    """
    if lst:
        return lst[0]
    else:
        return None
