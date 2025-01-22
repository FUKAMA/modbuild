import argparse
import importlib
import pkgutil
import tkinter
import os
import runpy
import subprocess
from tkinter import Tk, filedialog
from pathlib import Path
import sys


import loadPack

# このパッケージの説明



def LoadSubPackages(parser):

    packHelp = "パッケージの説明"

    loadPack.Load(parser,__path__,__name__,packHelp)
