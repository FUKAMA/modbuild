import pkgutil
import importlib
import subprocess
import os
from tkinter import Tk, filedialog
import requests
import zipfile
import json

def LoadSubcommands():
    """
    `commands` ディレクトリ内のすべてのモジュールを探索して動的にインポートする。
    """
    commands = {}
    # このパッケージの名前を取得
    package_name = __name__

    # このパッケージのすべてのモジュールを探索
    for loader, module_name, is_pkg in pkgutil.iter_modules(__path__):
        # モジュールを動的にインポート
        full_module_name = f"{package_name}.{module_name}"
        module = importlib.import_module(full_module_name)

        # モジュールが `add_subcommand` を定義している場合のみ登録
        if hasattr(module, "Register"):
            commands[module_name] = module

    return commands

