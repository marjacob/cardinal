# -*- coding: utf-8 -*-

"""
This module contains the interface required to implement the Command pattern.
"""

import abc


class ITask(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def execute(self):
        raise NotImplementedError()
    @abc.abstractproperty
    def result(self):
        raise NotImplementedError()
