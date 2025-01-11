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
    print("モジュールのビルド")
    subprocess.run(["cmake","--build","."])

    # ビルド結果が格納されているディレクトリに移動
    os.chdir("build/bin/Debug")

    # テストを実行
    os.system(f"test.exe --gtest_filter={args.case}.{args.name}")

