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
    
    os.chdir("/build")

    subprocess.run(["ctest","--output-on-failure"])
    
    # print(f"Building project: {args.name}, type: {args.type}")
