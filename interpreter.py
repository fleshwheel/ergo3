#!/usr/bin/env python3
# -*- encoding: utf-8 *-*

import os
from typing import *
from executable_handler import command_in_path, run_command

def ergo_add(a, b):
    return Num(a.value + b.value)

def ergo_sub(a, b):
    return Num(a.value - b.value)

def ergo_print(a):
    if isinstance(a.ergo_type, tuple):
        if a.ergo_type[0] == "list":
            for item in a.values:
                print(item)
    
    elif a.ergo_type == "num":
        print(a.value)
    elif a.ergo_type == "str":
        print(a.value)
    elif a.ergo_type == "list":
        for item in a.values:
            ergo_print(item)
    return Null()

sample_namespace = {
    "+": (Function(("num", "num"), "num", ergo_add)),
    "-": (Function(("num", "num"), "num", ergo_sub)),
    "print": (Function(("any",), "null", ergo_print)),
}


def state_def(state):
    def inner(key, value):
        state.namespace[key] = value
    return inner

state_functions = {
    "def": lambda state: (Function(("symbol",), "any", state_def(state)))
}

class ErgonomicaState:
    def __init__(self, namespace = sample_namespace,
                 types = {},
                 alive = True):
        self.namespace = namespace
        self.types = types
        self.alive = alive
        for fname in state_functions:
            self.namespace[fname] = state_functions[fname](self)
        
def eval(ast, state = ErgonomicaState(), resolve_symbols = True):

    if isinstance(ast, Symbol) and resolve_symbols:
        if ast in state.namespace:
            return state.namespace[ast]
        else:
            raise NameError("no such symbol " + str(ast))
    
    if not isinstance(ast, list): return ast

    # *NOTE*
    # here is where i will implement lambda functions --
    # simply bypass the lookup when the car is a list.
    # type checking code (should) remain the same.
    
    car, cdr = ast[0], ast[1:]
    for (i, arg) in enumerate(cdr):
        cdr[i] = eval(arg)

    if car not in state.namespace:
        if command_in_path(car):
            return List("str", run_command(car, [str(arg) for arg in cdr]))
        raise NameError(f":3 function not found: {car}")
    
    function = state.namespace[car]

    assert isinstance(function, Function)

    if len(function.domain) != len(cdr):
        raise TypeError("ergo > typing: too few arguments provided to " + str(function))

    for (sig, arg) in zip(function.domain, cdr):
        assert type_compare(sig, arg)

    ret = function.obj(*[eval(arg) for arg in cdr])

    if not type_compare(function.codomain, ret):
        raise TypeError("invalid return type! signature = " + str(signature))
        
    return ret
    
