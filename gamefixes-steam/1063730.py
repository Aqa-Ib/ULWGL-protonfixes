""" Game fix for New World
"""
#pylint: disable=C0103

import glob
import os
import subprocess
from protonfixes import util

def main():
    """ Needs core count limit
    """
    # Fix the startup process:
    util.set_cpu_topology_limit(12)

