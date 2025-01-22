import argparse
import importlib
import pkgutil
import os
import runpy
import os
import sys
import subprocess
from tkinter import filedialog
from tkinter import Tk, filedialog

# このパッケージの説明
import clitemp


def LoadSubPackages(parser):

    packHelp = "パッケージの説明"

    clitemp.Load(parser,__path__,__name__,packHelp)
