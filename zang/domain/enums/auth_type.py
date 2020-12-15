# -*- coding: utf-8 -*-

"""
zang.domain.enums.auth_type
~~~~~~~~~~~~~~~~~~~
Module containing `AuthType` available options
"""
from enum import Enum


class AuthType(Enum):
    IP_ACL = 'ip_acl'
    CREDENTIAL_LIST = 'credential_list'
    NO_TRAFFIC = 'no_traffic'
    IP_AND_CREDENTIAL = 'ip_and_credential'
