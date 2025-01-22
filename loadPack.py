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


# このパッケージの説明



def Load(parser,dirPath,dirName,packHelp):
    # 今いるディレクトリの中にあるアイテムを全て走査
    for loader, name, isPkg in pkgutil.iter_modules(dirPath):

        # 今のディレクトリの名前を取得
        modName = f"{dirName}.{name}"
        # モジュールをインポート
        module = importlib.import_module(modName)

        if hasattr(module, "Register"):
            module.Register(parser)

        if hasattr(module, "LoadSubPackages"):

            # 
            packParser = parser.add_parser(f"{name}",help = f"pck: {packHelp}")
            subParser = packParser.add_subparsers()
            module.LoadSubPackages(subParser)

