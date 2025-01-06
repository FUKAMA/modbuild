#!/usr/bin/env python3
#========================================================
# エントリポイントとなるコードを記述するファイル
#========================================================

# コマンドライン引数を処理するための機能をインポート
import argparse

# コマンドのパッケージをインポート
from commands import LoadSubcommands

def main():
    # コマンドライン引数を収集
    parser = argparse.ArgumentParser(description="サブコマンドを指定")
    subparsers = parser.add_subparsers(dest="command", help="サブコマンド")

    # commandsディレクトリ内のサブコマンドを収集
    commands = LoadSubcommands()
    # 収集したサブコマンドを全て走査
    for name, module in commands.items():
        # サブコマンドを初期化
        module.Register(subparsers)

    # 引数を解析
    args = parser.parse_args()

    # サブコマンドを実行
    if args.command and args.command in commands:
        commands[args.command].Execute(args)
    else:
        parser.print_help()

# エントリポイント
if __name__ == '__main__':
    main()

