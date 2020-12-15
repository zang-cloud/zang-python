# -*- coding: utf-8 -*-

"""
zang.domain.enums.call_direction
~~~~~~~~~~~~~~~~~~~
Module containing `CallDirection` available options
"""
from enum import Enum


class CallDirection(Enum):
    INBOUND = 'inbound'
    INBOUND_SIP = 'inbound-sip'
    INBOUND_CLIENT = 'inbound-client'
    INTER_CLIENT = 'inter-client'
    OUTBOUND_API = 'outbound-api'
    OUTBOUND_DIAL = 'outbound-dial'
    OUTBOUND_SIP = 'outbound-sip'
    UNKNOWN = 'unknown'
