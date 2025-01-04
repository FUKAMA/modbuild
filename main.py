#!/usr/bin/env python3
#========================================================
# エントリポイントとなるコードを記述するファイル
#========================================================

# コマンドライン引数を処理するための機能をインポート
import argparse

# コマンドのパッケージをインポート
from commands import load_commands

def main():
    # コマンドライン引数を収集
    parser = argparse.ArgumentParser(description="コマンドライン引数を収集")
    subparsers = parser.add_subparsers(dest="command", help="サブコマンド")

    # commands ディレクトリ内のサブコマンドをロード
    commands = load_commands()
    for name, module in commands.items():
        print(f"Loading subcommand: {name}")
        module.add_subcommand(subparsers)

    # 引数を解析
    args = parser.parse_args()

    # サブコマンドを実行
    if args.command and args.command in commands:
        commands[args.command].execute(args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()

