import pkgutil
import importlib
import subprocess
import os
from tkinter import Tk, filedialog
import requests
import zipfile
import json
import argparse
import importlib


def LoadSubcommands(allCommands, subparsers):
    print("UOOOOOOOOOOOOOOO")
    """
    このパッケージの説明
    """
    hintString = "このパッケージの説明"
    """
    このパッケージの説明を入力
    """

    # ディレクトリの名前からパッケージ名を取得
    dirName = "C:\Project\modbuild\commands"
    print(dirName)
    parser = subparsers.add_parser(dirName) 

    # このパッケージの名前を取得
    package_name = __name__

    # 今のディレクトリにある要素を全て検索
    for item in os.listdir(dirName):
        full_path = os.path.join(dirName, item)  # フルパスを生成

        # アイテムがモジュールファイルなら
        if os.path.isfile(full_path) and item.endswith(".py") and item != "__init__.py":            # モジュールの名前を取得
            commandName = item[:-3]  # ".py" を除外
            full_module_name = f"{package_name}.{commandName}"
            
            print(full_path)
            print(commandName)
            
            # モジュールを動的にインポート
            full_module_name = f"{package_name}.{commandName}"
            print(full_module_name)
            # モジュールの名前とコマンド名を保存
            allCommands[commandName] = full_module_name
            parser.add_parser(commandName, help = hintString) 

        # アイテムがディレクトリの場合
        if os.path.isdir(full_path) and "__init__.py" in os.listdir(full_path):
            print(full_path)

            full_module_name = f"{package_name}.{item}"
            initMod = importlib.import_module(full_module_name)
            print(full_module_name)
            initMod.LoadSubcommands(allCommands, parser)
    
    print("endInit")


    # # このパッケージのすべてのモジュールを探索
    # for loader, module_name, is_pkg in pkgutil.iter_modules(__path__):
    #     # モジュールを動的にインポート
    #     full_module_name = f"{package_name}.{module_name}"
    #     # モジュールの名前とコマンド名を保存
    #     commands[module_name] = full_module_name



    #     parser.add_parser(module_name, help="プロジェクトにソースファイルを追加する") 

        
    #     # さらに下位のパッケージがあればロードする
    #     LoadSubcommands(commands, parser)



# def LoadSubcommands():
#     """
#     `commands` ディレクトリ内のすべてのモジュールを探索して動的にインポートする。
#     """
#     commands = {}
#     # このパッケージの名前を取得
#     package_name = __name__

#     # このパッケージのすべてのモジュールを探索
#     for loader, module_name, is_pkg in pkgutil.iter_modules(__path__):
#         # モジュールを動的にインポート
#         full_module_name = f"{package_name}.{module_name}"
#         module = importlib.import_module(full_module_name)

#         # モジュールが `add_subcommand` を定義している場合のみ登録
#         if hasattr(module, "Register"):
#             commands[module_name] = module
#     return commands