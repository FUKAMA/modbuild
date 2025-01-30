import argparse
import importlib
import pkgutil
import tkinter
import os
import runpy
import requests
import os
import subprocess
from tkinter import filedialog
from tkinter import Tk, filedialog
import json


import clitemp
from modules import fileUtl

# このパッケージの説明



def LoadSubPackages(parser):

    packHelp = "モジュール専用の操作コマンドが格納されたパッケージ"

    clitemp.Load(parser,__path__,__name__,packHelp)
