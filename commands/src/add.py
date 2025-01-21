import os
import sys
import subprocess
from tkinter import filedialog
from tkinter import Tk, filedialog

from modules import utl


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
    commName =os.path.splitext(os.path.basename(os.path.abspath(__file__)))[0] 
    parser = subparsers.add_parser(f"{commName}", help=f"cmm: {helpString}")
    
    
    #=====================================
    # 引き数定義ゾーン開始
    #--------------
    # parser.add_argument("--変数名", help="変数の説明")
    #--------------
    parser.add_argument("--name", help="追加するファイルの名前")
    parser.add_argument("--dir",default="",help="ソースを配置するディレクトリ")
    parser.add_argument("-hpp", action="store_true", help="ヘッダファイルを生成")
    parser.add_argument("-cpp", action="store_true", help="ヘッダファイルを生成")
    #--------------
    # 引き数定義ゾーン終了
    #=====================================

# コマンドを実行したときの処理
def Execute(args):

    utl.aaa()

    # ディレクトリが指定されてなければエクスプローラーを開いて指定
    print(args.name)
    # プロジェクトのあるディレクトリを保存
    cDir = os.path.abspath(os.getcwd())
    # ディレクトリを選択
    fileDir = filedialog.askdirectory(initialdir = f"{cDir}/main/src")
    # ディレクトリを移動
    os.chdir(fileDir)

    # ファイルに書き込む文字列を作成
    hFileString=f"#pragma once\n// {args.name}"
    cppFileString=""

    # if args.h:
    #     # ファイルを作成
    #     with open(f"{args.name}.h",mode="w") as file:
    #         file.write(hFileString)
    if args.hpp:
        # ファイルを作成
        with open(f"{args.name}.hpp",mode="w") as file:
            file.write(hFileString)
    if args.cpp:
        # ファイルを作成
        with open(f"{args.name}.cpp",mode="w") as file:
            if args.hpp:
            # if args.h or args.hpp:
                cppFileString=f"#include \"{args.name}.hpp\""
            file.write(cppFileString)

    # ディレクトリを戻す
    os.chdir(cDir)

    # プロジェクトを更新
    files = os.listdir(os.getcwd()+"/main/include")
    projName = [i for i in files if i.endswith(".hpp") == True]
    subprocess.run(["cmake",f"-DPROJ_NAME={os.path.splitext(projName[0])[0]}","-DPROJ_TYPE=STATIC"])
