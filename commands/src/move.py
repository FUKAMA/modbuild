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
    helpString = "ソースファイルを移動するコマンド"
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
    parser.add_argument("--file", default="",help="位置を変更するファイル")
    parser.add_argument("--dir", default="",help="変更先のディレクトリ")
    parser.add_argument("-test", action = "store_true", help = "テストも一緒に移動するか")
    #--------------
    # 引き数定義ゾーン終了
    #=====================================

# コマンドを実行したときの処理
def Execute(args):

    if not proj.IsProject():
        log.Error("プロジェクトディレクトリではありません")
        return False

    # ディレクトリが指定されてなければエクスプローラーを開いて指定
    # プロジェクトのあるディレクトリを保存
    cDir = os.path.abspath(os.getcwd())
    # srcディレクトリのパスを作成
    srcDir = f"{cDir}/main/src"
    # エクスプローラーを開いてファイルを選択
    remFilePath = fileUtl.GetFilePathFromExplorer(srcDir)

    # ファイルが存在するか確認
    if fileUtl.IsExistFilePath(remFilePath):
        log.Error("存在しないファイルパスです")
        return False
    
    # ファイルを削除する
    os.remove(remFilePath)


    # ディレクトリを戻す
    os.chdir(cDir)

    # プロジェクトを更新
    proj.UpdateProject()

