#==================================================
# サブコマンドを作成する際にベースとなる形式が記述されているファイル
#==================================================

import subprocess
import fnmatch
import os
from tkinter import filedialog
from tkinter import Tk, filedialog
import pathlib
from pathlib import Path

def Register(subparsers):
    parser = subparsers.add_parser("addtest", help="テストを作成する")
    # parser.add_argument("--name", help="追加するファイルの名前")


def Execute(args):

    # ディレクトリが指定されてなければエクスプローラーを開いて指定
    # print(args.name)
    # プロジェクトのあるディレクトリを保存
    cDir = os.path.abspath(os.getcwd())
    # ディレクトリを選択
    fileDir = filedialog.askopenfilename(
        title="テスト対象のファイルを指定",
        filetypes=[
            ("ヘッダファイル", "*.hpp")
            ])
    print(fileDir)

    fileObj=Path(fileDir).resolve()

    # テストを作成するソースファイルの名前
    sourceName =os.path.splitext(os.path.basename(fileDir))[0]

    # mainのsrcまで移動
    os.chdir("main/src")
    # srcからの相対パスを求める
    mainRelPath =fileObj.relative_to(os.getcwd())
    print(mainRelPath)

    # testのsrcまで移動
    os.chdir(cDir)
    os.chdir("test/src")
    # 相対パスを使いtestのsrcからの絶対パスを作成
    testPath = os.getcwd() + f"\{mainRelPath}"

    print(testPath)
    testDir=os.path.dirname(testPath)
    print(testDir)

    os.mkdir(testDir)

    # ディレクトリを移動
    os.chdir(testDir)

    # テストファイルに書き込む文字列を作成

    testSource = f"#include <gtest/gtest.h>\n\
#include \"{mainRelPath}\"\n\
TEST({sourceName}, AAA)\n\
{{\n\
    EXPECT_TRUE(true);    // 成功\n\
}}\n\
"

    # ファイルを作成
    with open(f"{sourceName}.cpp",mode="w") as file:
        file.write(testSource)

    # ファイルに書き込む文字列を作成
    # hFileString=f"#pragma once\n// {args.name}"
    # cppFileString=""

    # if args.hpp:
    # if args.cpp:
    #     # ファイルを作成
    #     with open(f"{args.name}.cpp",mode="w") as file:
    #         if args.hpp:
    #         # if args.h or args.hpp:
    #             cppFileString=f"#include \"{args.name}.hpp\""
    #         file.write(cppFileString)

    # ディレクトリを戻す
    os.chdir(cDir)

    # プロジェクトを更新
    files = os.listdir(os.getcwd()+"/main/include")
    projName = [i for i in files if i.endswith(".hpp") == True]
    subprocess.run(["cmake",f"-DPROJ_NAME={os.path.splitext(projName[0])[0]}","-DPROJ_TYPE=STATIC"])

    # update.Execute(args)
    # subprocess.run(["cmake",f"-DPROJ_NAME={args.name}",f"-DPROJ_TYPE=STATIC"])



    # print(f"Building project: {args.name}, type: {args.type}")