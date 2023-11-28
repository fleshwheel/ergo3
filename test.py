#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""
Test REPL for Ergo3. I will build a shell interface using Python Prompt Toolkit.
"""

import os
import traceback
from parser import parse
from tokenizer import tokenize
from interpreter import eval, ErgonomicaState, ergo_print

state = ErgonomicaState()

test_code = "print (ls)"

eval(parse(tokenize(test_code)), state)

while state.alive:
    code = input("ergo :3 $")
    if code.strip() == "":
        continue
    try:
        ergo_print(eval(parse(tokenize(code)), state))
    except Exception:
        print(traceback.format_exc())


