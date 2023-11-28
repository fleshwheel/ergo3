#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import os
import subprocess
from functools import reduce

def command_in_path(command):
    dirs_in_path = os.environ["PATH"].split(":")
    return command in reduce(lambda a, b: a + b,
                             (os.listdir(dir) for dir in dirs_in_path))

def run_command(command, args):
    """
    A very minimal interface for running commands. This function does not use Ergonomica
    typing.
    """
    try:
        p = subprocess.Popen([command] + args, stdout=subprocess.PIPE, universal_newlines=True)
        p.wait()
        cur = [line[:-1].encode().decode('utf-8') for line in iter(p.stdout.readline, "")]
        return cur

    except KeyboardInterrupt as e:
        p.terminate()
        raise e

    # TODO: instead of checking for a FileNotFoundError, check if the command is in the user's PATH.
    except FileNotFoundError as e:
        raise ErgonomicaError("[ergo]: Unknown command '{}'.".format(x[0]))

    except OSError as e: # on Python2
        raise ErgonomicaError("[ergo]: Unknown command '{}'.".format(x[0]))

