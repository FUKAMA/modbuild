#==================================================
# モジュールのテストを実行するサブコマンド
#==================================================

import subprocess
import os
def Register(subparsers):
    parser = subparsers.add_parser("test", help="テストを実行する")
    parser.add_argument("--case", default="*",help="実行するテストケース")
    parser.add_argument("--name", default="*",help="実行するテスト名")

def Execute(args):

    # モジュールをビルド
    subprocess.run(["cmake","--build","."])
    
    # os.chdir("build")
    os.chdir("build/bin/Debug")

    # subparsers.run("test.exe")

    os.system(f"test.exe --gtest_filter={args.case}.{args.name}")

    # subprocess.run(["ctest","--output-on-failure"])
    
    # print(f"Building project: {args.name}, type: {args.type}")
