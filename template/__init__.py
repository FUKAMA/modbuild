import argparse
import importlib
import pkgutil
import tkinter
import os
import runpy

# このパッケージの説明



def LoadSubPackages(parser):

    packHelp = "パッケージの説明"

    # 今いるディレクトリの中にあるアイテムを全て走査
    for loader, name, isPkg in pkgutil.iter_modules(__path__):

        # 今のディレクトリの名前を取得
        modName = f"{__name__}.{name}"
        # モジュールをインポート
        module = importlib.import_module(modName)
        runpy.run_module(modName, run_name="__main__", alter_sys=True)


        if hasattr(module, "Register"):
            module.Register(parser)

        if hasattr(module, "LoadSubPackages"):

            # 
            packParser = parser.add_parser(f"{name}",help = f"pck: {packHelp}")
            subParser = packParser.add_subparsers()
            module.LoadSubPackages(subParser)

