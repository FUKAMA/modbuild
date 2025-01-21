#!/usr/bin/env python3
#========================================================
# エントリポイントとなるコードを記述するファイル
#========================================================

# コマンドライン引数を処理するための機能をインポート
import argparse
import importlib
import importlib.util
import sys

from modules.util import log

from commands import LoadSubPackages

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
        log.Error("コマンドが指定されていません。",True)

    # コマンドライン引数を解析してcmmandとargsに分割
    clArgs = clArgParsers.parse_args()

    # 
    if not clArgs:
        log.Error("コマンドが指定されていません。",True)

    # 
    if not clArgs.command:
        log.Error("コマンドが指定されていません。",True)
    
    # 実行するコマンドの名前(パス)を作成
    modName = "commands." + ".".join(clArgs.command)

    # コマンドが存在しなければ終了
    if importlib.util.find_spec(modName) is None:
        log.Error("存在しないコマンドです",True)


    # コマンドライン引数を解析して指定したコマンドの引数を取得
    cmArgs = cmArgParsers.parse_args()
    module = importlib.import_module(modName)


    # 指定したモジュールがコマンドなら
    if hasattr(module, "Execute"):
        module.Execute(cmArgs)

    # 指定したモジュールがパッケージのInitなら
    else:
        log.Error("パッケージは実行できません コマンドを指定してください",True)



# エントリポイント
if __name__ == '__main__':
    main()
