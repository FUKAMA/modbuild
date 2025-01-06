#==================================================
# 新規モジュールの開発環境を構築するサブコマンド
#==================================================

import subprocess
import os

def Register(subparsers):
    parser = subparsers.add_parser("create", help="モジュールの開発環境を作成する")
    parser.add_argument("--name", required=True, help="プロジェクトの名前")
    parser.add_argument("--type", choices=["STATIC", "SHARED"], default="STATIC", help="プロジェクトの種類")

def Execute(args):
    print(f"Building project: {args.name}, type: {args.type}")

    # モジュールのテンプレートリポジトリをクローンしてくる
    subprocess.run(["git","clone","https://github.com/FUKAMA/TempModule.git",f"{args.name}"])

    # プロジェクトを作成
    os.chdir(f"{args.name}")
    subprocess.run(["cmake",f"-DPROJ_NAME={args.name}",f"-DPROJ_TYPE={args.type}"])