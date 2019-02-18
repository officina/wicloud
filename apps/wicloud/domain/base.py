from typing import List, Optional

class BaseDomainEntity(object):
    def __init__(self, **kwargs):
        if "dictObject" in kwargs.keys():
            for field in (kwargs['dictObject']):
                if field in self.__dict__:
                    self.__dict__[field] = kwargs['dictObject'][field]
        else:
            for field in (kwargs.keys()):
                if field in self.__dict__:
                    self.__dict__[field] = kwargs.get(field, None)
