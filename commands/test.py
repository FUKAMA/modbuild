#==================================================
# モジュールのテストを実行するサブコマンド
#==================================================

import subprocess
import os
def Register(subparsers):
    parser = subparsers.add_parser("test", help="テストを実行する")
    # parser.add_argument("--testCase", required=True, help="Project name")

def Execute(args):

    # モジュールをビルド
    subprocess.run(["cmake","--build","."])
    
    # os.chdir("build")
    os.chdir("build/bin/Debug")

    # subparsers.run("test.exe")

    os.system("test.exe")

    # subprocess.run(["ctest","--output-on-failure"])
    
    # print(f"Building project: {args.name}, type: {args.type}")
