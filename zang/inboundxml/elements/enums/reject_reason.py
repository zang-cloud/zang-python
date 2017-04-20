# -*- coding: utf-8 -*-

"""
zang.domain.enums.reject_reason
~~~~~~~~~~~~~~~~~~~
Module containing `RejectReason` available options
"""

from enum import Enum


class RejectReason(Enum):
    BUSY = 'busy'
    REJECTED = 'rejected'
