# -*- coding: utf-8 -*-

"""
zang.inboundxml.elements.refer
~~~~~~~~~~~~~~~~~~~
Module containing `Refer` inbound xml element
"""

from zang.inboundxml.elements.base_node import BaseNode
from zang.inboundxml.elements.sip import Sip

import sys
if sys.version_info > (3, 0):
    str_classes = (str, bytes)


class Refer(BaseNode):

    _allowedContentClass = (
        str,
        int,
        Sip,
    )

    def __init__(
            self,
            address=None,
            action=None,
            method=None,
            timeout=None,
            callbackUrl=None,
            callbackMethod=None,):
        self._value = address
        self.action = action
        self.method = method
        self.timeout = timeout
        self.callbackUrl = callbackUrl
        self.callbackMethod = callbackMethod

        self._content = []

    @property
    def address(self):
        return self._value

    @address.setter
    def address(self, value):
        if value is None:
            raise TypeError
        self._value = value

    @property
    def elements(self):
        return self._content

    def addElement(self, element):
        if isinstance(element, type(self)._allowedContentClass):
            self._content.append(element)
        else:
            raise TypeError('Element not allowed for content model')

    def removeElementAtIndex(self, index):
        del self._content[index]
