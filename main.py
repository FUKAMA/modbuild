#!/usr/bin/env python3
#========================================================
# エントリポイントとなるコードを記述するファイル
#========================================================

# コマンドライン引数を処理するための機能をインポート
import argparse
import importlib
import importlib.util
import tkinter
import sys


# コマンドのパッケージをインポート
# from commands import addsource

from commands import LoadSubPackages

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
SKY = "\033[96m"
RESET = "\033[0m"

def Error(message):
    print(f"{RED}{message}{RESET}", file=sys.stderr)
    sys.exit(1)

def main():

    # コマンドライン引数を解析するためのparser
    clArgParsers = argparse.ArgumentParser()
    clArgParsers.add_argument("command", nargs="+", help="コマンドを入力")
    clArgParsers.add_argument("args", nargs=argparse.REMAINDER, help="コマンドに渡す引数")
    
    # コマンドの引数などを解析するためのparser
    cmArgParsers = argparse.ArgumentParser()
    subParser = cmArgParsers.add_subparsers(dest="subcommand", required=False)
    LoadSubPackages(subParser)
    
    
    # コマンドが指定されてなければ終了
    if len(sys.argv) < 2:
        Error("コマンドが指定されていません。")

    # コマンドライン引数を解析してcmmandとargsに分割
    clArgs = clArgParsers.parse_args()

    # 
    if not clArgs:
        Error("コマンドが指定されていません。")

    # 
    if not clArgs.command:
        Error("コマンドが指定されていません。")
    
    # 実行するコマンドの名前(パス)を作成
    modName = "commands." + ".".join(clArgs.command)

    # コマンドが存在しなければ終了
    if importlib.util.find_spec(modName) is None:
        Error("存在しないコマンドです")


    # コマンドライン引数を解析して指定したコマンドの引数を取得
    cmArgs = cmArgParsers.parse_args()
    module = importlib.import_module(modName)


    # 指定したモジュールがコマンドなら
    if hasattr(module, "Execute"):
        module.Execute(cmArgs)

    # 指定したモジュールがパッケージのInitなら
    else:
        Error("パッケージは実行できません コマンドを指定してください")



# エントリポイント
if __name__ == '__main__':
    main()
