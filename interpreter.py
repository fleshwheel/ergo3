#!/usr/bin/env python3
# -*- encoding: utf-8 *-*

import os
from typing import *

def ergo_add(a, b):
    return Num(a.value + b.value)

def ergo_print(a):
    if a.ergo_type == "num":
        print(a.value)
    elif ergo_type == "str":
        print(a.value)

sample_namespace = {
    "add": (("func", "num", "num", "num"), ergo_add),
    "print": (("func", "num", "none"), ergo_print)
}

class ErgonomicaState:
    def __init__(self, namespace = sample_namespace,
                 types = {},
                 alive = True):
        self.namespace = namespace
        self.types = types
        self.alive = alive


def eval(ast, state = ErgonomicaState()):
    if isinstance(ast, list):
        car, cdr = ast[0], ast[1:]

        # *NOTE*
        # here is where i will implement lambda functions --
        # simply bypass the lookup when the car is a list.
        # type checking code (should) remain the same.
        
        if car not in state.namespace:
            raise NameError(f":3 function not found: {car}")
        
        signature, function = state.namespace[car]

        assert signature[0] == "func"

        assert len(signature) == len(cdr) + 2

        for (sig, arg) in zip(signature[1:], cdr):
            assert type_compare(sig, arg)


        # TODO
        # check function return type
        return function(*[eval(arg) for arg in cdr])
    else:
        return ast
    
