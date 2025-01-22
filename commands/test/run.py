import subprocess
import os

import clitemp

# 説明や引き数などを登録する
def Register(subparsers):
    #=====================================
    # 引き数定義ゾーン開始
    #--------------
    # ↓ここにこのコマンドの説明を書く
    helpString = "テンプレートコマンド"
    #--------------
    # 引き数定義ゾーン終了
    #=====================================

    
    # コマンド名をファイル名から取得
    parser = clitemp.CreateCommandParser(__file__,subparsers, helpString)
    
    
    #=====================================
    # 引き数定義ゾーン開始
    #--------------
    # parser.add_argument("--変数名", help="変数の説明")
    #--------------
    parser.add_argument("--case", default="*",help="実行するテストケース")
    parser.add_argument("--name", default="*",help="実行するテスト名")
    #--------------
    # 引き数定義ゾーン終了
    #=====================================

# コマンドを実行したときの処理
def Execute(args):

    # モジュールをビルド
    print("モジュールのビルド")
    subprocess.run(["cmake","--build","."])

    # ビルド結果が格納されているディレクトリに移動
    os.chdir("build/bin/Debug")

    # テストを実行
    os.system(f"test.exe --gtest_filter={args.case}.{args.name}")

