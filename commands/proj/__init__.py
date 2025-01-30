import argparse
import importlib
import pkgutil
import tkinter
import os
import runpy
import sys
import subprocess
import sys
import json

import clitemp
from modules import fileUtl

# このパッケージの説明



def LoadSubPackages(parser):

    packHelp = "パッケージの説明"

    clitemp.Load(parser,__path__,__name__,packHelp)
