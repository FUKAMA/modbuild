import os
import sys
import subprocess
from tkinter import filedialog
from tkinter import Tk, filedialog

from modules.utl import log
from modules import fileUtl
from modules import proj
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
    parser = clitemp.CreateCommandParser(__file__, subparsers, helpString)
    
    #=====================================
    # 引き数定義ゾーン開始
    #--------------
    # parser.add_argument("--変数名", help="変数の説明")
    #--------------
    parser.add_argument("--name", help="追加するファイルの名前")
    parser.add_argument("--dir",default="",help="ソースを配置するディレクトリ")
    parser.add_argument("-hpp", action="store_true", help="ヘッダファイルを生成")
    parser.add_argument("-cpp", action="store_true", help="ヘッダファイルを生成")
    parser.add_argument("-open", action = "store_true", help = "ファイル追加後に開くか")
    #--------------
    # 引き数定義ゾーン終了
    #=====================================

# コマンドを実行したときの処理
def Execute(args):

    if not proj.IsProject():
        log.Error("プロジェクトディレクトリではありません")
        return False

    if not args.name:
        log.Error("ファイル名を指定してください")
        return False
    if not (args.hpp or args.cpp):
        log.Error("ファイルの種類を指定してください")
        return False

    # ディレクトリが指定されてなければエクスプローラーを開いて指定
    print(args.name)
    # プロジェクトのあるディレクトリを保存
    cDir = os.path.abspath(os.getcwd())

    # srcディレクトリのパスを作成
    srcDir = f"{cDir}/main/src"

    # ディレクトリを選択
    fileDir = fileUtl.GetDirPathFromExplorer(srcDir)

    # ディレクトリを移動
    os.chdir(fileDir)

    # ファイルに書き込む文字列を作成
    hFileString = f"#pragma once\n"

    filePath = ""

    fullFilePath = ""

    # ファイルを作成
    if args.hpp:
        filePath = f"{args.name}.hpp"
        fileUtl.CreateFile(path = filePath,value=hFileString)
        # テストファイルの絶対パスを求める
        fullFilePath = fileDir + "/" + filePath
    if args.cpp:
        filePath = f"{args.name}.cpp"
        hFileString = ""
        if args.hpp:
            hFileString=f"#include \"{args.name}.hpp\""
        fileUtl.CreateFile(path=filePath,value=hFileString)
        # テストファイルの絶対パスを求める
        fullFilePath = fileDir + "/" + filePath
    

    # ディレクトリを戻す
    os.chdir(cDir)

    # プロジェクトを更新
    proj.UpdateProject()


    if args.open:
        fileUtl.OpenFile(fullFilePath)

