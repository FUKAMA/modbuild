import argparse
import importlib
import pkgutil
import tkinter
import os
import runpy
import sys
import subprocess
import sys


# このパッケージの説明



def LoadSubPackages(parser):

    packHelp = "パッケージの説明"

    # 今いるディレクトリの中にあるアイテムを全て走査
    for loader, name, isPkg in pkgutil.iter_modules(__path__):

        # 今のディレクトリの名前を取得
        modName = f"{__name__}.{name}"
        # モジュールをインポート
        module = importlib.import_module(modName)


        if hasattr(module, "Register"):
            module.Register(parser)

        if hasattr(module, "LoadSubPackages"):

            # 
            packParser = parser.add_parser(f"{name}",help = f"pck: {packHelp}")
            subParser = packParser.add_subparsers()
            module.LoadSubPackages(subParser)

