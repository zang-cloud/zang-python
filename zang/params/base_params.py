from enum import Enum


class BaseParams(object):

    def __init__(self):
        self._pathParams = {}
        self._bodyParams = {}
        self._queryParams = {}

    @property
    def data(self):
        return BaseParams.filterParams(self._bodyParams)
        # data_ = {}
        # for param, value in self._bodyParams.iteritems():
        #     if value != None:
        #         data_[param] = value
        # return data_

    @property
    def params(self):
        return BaseParams.filterParams(self._queryParams)
        # params_ = {}
        # for param, value in self._queryParams.iteritems():
        #     if value != None:
        #         params_[param] = value
        # return params_

    @classmethod
    def filterParams(cls, params):
        params_ = {}
        for param, value in params.iteritems():
            if value != None:
                if isinstance(value, Enum):
                    value = value.value
                params_[param] = value
        return params_