# -*- coding: utf-8 -*-

"""
zang.domain.enums.call_direction
~~~~~~~~~~~~~~~~~~~
Module containing `CallDirection` available options
"""

from enum import Enum


class CallDirection(Enum):
    IN = 'in'
    OUT = 'out'
    BOTH = 'both'
