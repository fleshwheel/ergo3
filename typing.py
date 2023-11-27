#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

types = {
    "num": lambda: lambda o: o.ergo_type == "num",
    "str": lambda: lambda o: o.ergo_type == "str",
    "list": lambda t: lambda o: all([types[t] == o.ergo_type]),
    "func": lambda d, c: lambda o: (self.domain == d) and (self.codomain == c),
    "null": lambda: lambda o: o.type == "null"
}

class ImpossibleTypeException(Exception):
    pass

def typeof(ast):
    pass

def type_compare(signature, value):
    if isinstance(signature, list):
        # NOTE:
        # here is where i will enable function-like types
        pass
    else:
        return types[signature]()(value)

# base type
class ErgonomicaType:
    pass

class Null(ErgonomicaType):
    ergo_type = "null"
    def __init__(self):
        pass

# this one is kind of weird because i haven't quite
# seen numbers implemented this way in other languages.
# excited to see where it goes.
class Num(ErgonomicaType):
    ergo_type = "num"
    def __init__(self, value):
        if isinstance(value, int) or isinstance(value, float):
            self.value = value
            self.type = typeof(value)
        else:
            raise TypeError("Number must be instantiated with a value either of type `int` or `float`.")
    def __repr__(self):
        return "Num(" + str(self.value) + ")"
        
class Str(ErgonomicaType, str):
    ergo_type = "str"
    pass

class FunctionType:
    ergo_type = "func"
    def __init__(self, *args):
        self.domain = args[:-1]
        self.codomain = args[-1]

class ListType:
    ergo_type = "list"
    def __init__(self, t):
        self.t = t

class DictType:
    ergo_type = "dict"
    def __init__(self, k, v):
        self.k = k
        self.v = v




            
