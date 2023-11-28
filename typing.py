#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

types = {
    "any": lambda: lambda o: True,
    "num": lambda: lambda o: o.ergo_type == "num",
    "str": lambda: lambda o: o.ergo_type == "str",
    "list": lambda t: lambda o: all([types[t] == o.ergo_type]),
    "func": lambda d, c: lambda o: (self.domain == d) and (self.codomain == c),
    "null": lambda: lambda o: o.ergo_type == "null"
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
        if signature in types:
            return types[signature]()(value)
        else:
            raise TypeError("ergo > typing: unknown type \"" + signature + "\"")

# base type
class ErgonomicaType:
    pass

class Symbol(ErgonomicaType):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return "Symbol(" + self.name + ")"
        

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
    def __str__(self):
        return str(self.value)
        
class Str(ErgonomicaType, str):
    ergo_type = "str"
    def __init__(self, value):
        if isinstance(value, str):
            self.value = value
        else:
            raise TypeError("Str must be instantiated with a value of type `str`.")
    
    def __str__(self):
        return self.value

class Function:
    def __init__(self, domain, codomain, obj):
        self.domain = domain
        self.codomain = codomain
        self.obj = obj
        self.ergo_type = ("func", self.domain, self.codomain)
    def __repr__(self):
        return "Function(" + str(self.domain) + " -> " + str(self.codomain) + ")"

class List:
    def __init__(self, t, values):
        self.t = t
        self.values = values
        self.ergo_type = ("list", t)

class DictType:
    ergo_type = "dict"
    def __init__(self, k, v):
        self.k = k
        self.v = v




            
