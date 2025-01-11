#==================================================
# サブコマンドを作成する際にベースとなる形式が記述されているファイル
#==================================================

import subprocess
import fnmatch
import os
from tkinter import filedialog
from tkinter import Tk, filedialog

def Register(subparsers):
    parser = subparsers.add_parser("addsource", help="プロジェクトにソースファイルを追加する")
    parser.add_argument("--name", help="追加するファイルの名前")
    # parser.add_argument("--ext",choices=["h","cpp","hpp","hcpp"],default="hcpp",help="ファイルの拡張子")
    parser.add_argument("--dir",default="",help="ソースを配置するディレクトリ")
    # parser.add_argument("-h", action="store_true", help="ヘッダファイルを生成")
    parser.add_argument("-hpp", action="store_true", help="ヘッダファイルを生成")
    parser.add_argument("-cpp", action="store_true", help="ヘッダファイルを生成")


def Execute(args):

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

    # update.Execute(args)
    # subprocess.run(["cmake",f"-DPROJ_NAME={args.name}",f"-DPROJ_TYPE=STATIC"])



    # print(f"Building project: {args.name}, type: {args.type}")