# -*- coding: utf-8 -*-

"""
zang.inboundxml.elements..connect
~~~~~~~~~~~~~~~~~~~
Module containing `Connect` inbound xml element
"""

from zang.inboundxml.elements.base_node import BaseNode
from zang.inboundxml.elements.agent import Agent

class Connect(BaseNode):

    _allowedContentClass = (
        Agent,
    )

    def __init__(
            self,
            action=None,
            method=None):
        self.action = action
        self.method = method
        self._value = None
        self._content = []

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
