#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tokenizer import tokenize
from typing import *

def validate_symbol(symbol):
    """
    Throws appropriate exceptions on an invalid symbol.
    """

    return

def validate_flag(symbol):
    """
    Throws appropriate exceptions on an invalid flag.
    """

    return

class Symbol(str):
    def __new__(self, value):
        validate_symbol(value)
        return super(Symbol, self).__new__(self, value)

class Call():
    def __init__(self, car, cdr):
        self.car = car
        self.cdr = cdr

class Flag(str):
    def __new__(self, value):
        validate_flag(value)
        return super(Flag, self).__new__(self, value)    
    
def parse(tokens, allow_unclosed_blocks=False):
    depth = 0
    L = []
    parsed_command = False # switch set to true on first atom parsed---ensures that
                           # arguments after the command interpreted as strings
    parsed_tokens = []
    for token in tokens:
        if token.startswith("//"):
            continue
        if depth > 0:
            if token == ")":
                depth -= 1
            elif token == "(":
                parsed_command = True
                depth += 1
            if depth == 0:
                parsed_tokens.append(parse(L))
                L = []
            else:
                L.append(token)
            continue

        if token == "(":
            parsed_command = True
            depth = 1
            continue

        if not parsed_command:
            parsed_tokens.append(Symbol(token))
            parsed_command = True

        else:
            try:
                parsed_tokens.append(Num(int(token)))
            except ValueError:
                try:
                    parsed_tokens.append(Num(float(token)))
                except ValueError:
                    # it's a string or Symbol
                    if token.startswith("'") or token.startswith("\""):
                        parsed_tokens.append(Str(token.encode().decode("unicode-escape")[1:-1]))
                    else:
                        raise SyntaxError(token)
                        #parsed_token = token.encode().decode('unicode-escape')
                        #if parsed_token.startswith('-'):
                        #    parsed_token = Flag(parsed_token)
                        #parsed_tokens.append(parsed_token)


    if (L != []) and allow_unclosed_blocks:
        # i.e., there are some incomplete S-expressions. We want to allow
        # parsing this because it's necessary for the completion engine
        parsed_tokens.append(parse(L, allow_unclosed_blocks))

    return parsed_tokens

def file_lines(stdin):
    split_lines = [""]
    paren_depth = 0
    for line in stdin.split("\n"):
        line = line.strip()
        if line.startswith("#"):
            continue
        paren_depth += tokenize(line).count("(") - tokenize(line).count(")")
        if paren_depth == 0:
            split_lines[-1] += line
            split_lines.append("")
        else:
            split_lines[-1] += line
    return [x for x in split_lines if x]

def check_token(token):
    """Raise a SyntaxError on a malformed token."""
    if (token.startswith("'") and token.endswith("'")) or \
       (token.startswith("\"") and token.endswith("\"")):
        return
