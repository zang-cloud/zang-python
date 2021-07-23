# -*- coding: utf-8 -*-

"""
zang.inboundxml.elements.agent
~~~~~~~~~~~~~~~~~~~
Module containing `Agent` inbound xml element
"""

from zang.inboundxml.elements.base_node import BaseNode


class Agent(BaseNode):

    _allowedContentClass = ()

    def __init__(self, agentId):
        if agentId is None:
            raise TypeError
        self._value = agentId
        self._content = None

    @property
    def agent(self):
        return self._value

    @agent.setter
    def agent(self, value):
        if value is None:
            raise TypeError
        self._value = value
