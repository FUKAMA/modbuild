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

import loadPack

# このパッケージの説明



def LoadSubPackages(parser):

    packHelp = "パッケージの説明"

    loadPack.Load(parser,__path__,__name__,packHelp)
