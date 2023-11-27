#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""
Test REPL for Ergo3. I will build a shell interface using Python Prompt Toolkit.
"""

import traceback
from parser import parse
from tokenizer import tokenize
from interpreter import eval, ErgonomicaState

state = ErgonomicaState()

while state.alive:
    code = input("ergo :3 $")
    if code.strip() == "":
        continue
    try:
        eval(parse(tokenize(code)), state)
    except Exception:
        print(traceback.format_exc())


