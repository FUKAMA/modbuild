import os
import subprocess
from tkinter import Tk, filedialog
from pathlib import Path
import sys

import clitemp

from modules import fileUtl
from modules import proj
from modules.utl import log

# テストを追加するコマンド
# main/src/以下と同じ構成でtest/以下にテストを作成する
# 基本1ソースファイルにつき1テストファイルだが、 引数で
# 

# 説明や引き数などを登録する
def Register(subparsers):
    #=====================================
    # コマンドの説明ゾーン開始
    #--------------
    # ↓ここにこのコマンドの説明を書く
    helpString = "特定のファイルのテストを追加する"
    #--------------
    # コマンドの説明ゾーン終了
    #=====================================

    
    # コマンド名をファイル名から取得
    parser = clitemp.CreateCommandParser(__file__,subparsers, helpString)
    
    
    #=====================================
    # 引き数定義ゾーン開始
    #--------------
    # parser.add_argument("--変数名", help="変数の説明")
    #--------------
    parser.add_argument("--path", default = "", help = "テストを作成するソースファイル")
    parser.add_argument("--case", default = "", help = "テストケース名")
    parser.add_argument("-open", action = "store_true", help = "追加したファイルを開くか")
    #--------------
    # 引き数定義ゾーン終了
    #=====================================

# コマンドを実行したときの処理
def Execute(args):

    # if not args.case:
    #     log.Error("テスト名を指定してください")
    #     return

    # プロジェクトのあるディレクトリを保存
    cDir = os.path.abspath(os.getcwd())
    # メインプロジェクトのsrcディレクトリのパスを作成
    mainSrcDir = cDir + "/main/src"
    # テストプロジェクトのsrcのディレクトリのパスを作成
    testSrcDir = cDir + "/test/src"

    # もしテストを作成するファイルが指定されていなければ
    baseFilePath = args.path
    # エクスプローラーを開いてファイルを指定
    if not fileUtl.IsExistFilePath(baseFilePath):
        # エクスプローラーを開いてテストを作成するファイルを指定
        baseFilePath = fileUtl.GetFilePathFromExplorer(
            extList = [("ヘッダファイル", "*.hpp")],
            currentDir = mainSrcDir,
            titleText = "テストを作成するファイルを作成"
        )

        if not baseFilePath:
            log.Error("有効なパスを選択してください")
            return

    # 選択したソースファイルと同じ構成のtest/src版のディレクトリを作成し移動
    #---------------------------------

    # テスト対象のファイルパスをもとにパスオブジェクトを作成
    baseFileObj = Path(baseFilePath).resolve()
    # mainのsrcまで移動
    os.chdir(mainSrcDir)
    # srcからの相対パスを求める
    mainRelPath = baseFileObj.relative_to(os.getcwd())

    # testのsrcまで移動
    os.chdir(cDir)
    os.chdir(testSrcDir)

    # 相対パスを使いtestのsrcからの絶対パスとオブジェクトを作成
    testPath = os.getcwd() + f"/{mainRelPath}"
    testDir = os.path.dirname(testPath)

    # ディレクトリが存在しなければ作成
    testDirObject = Path(testDir)
    if not testDirObject.is_dir():
        os.mkdir(testDir)
    # テストディレクトリに移動
    os.chdir(testDir)


    # 作成したディレクトリにテストファイルを作成する
    #---------------------------------

    # テストを作成するソースファイルの名前
    sourceName = os.path.splitext(os.path.basename(baseFilePath))[0]

    caseName = args.case
    if caseName:
        caseName = "_" + args.case

    # テストファイルのファイル名
    testFilePath = sourceName + f"\{sourceName}" + caseName + "_test" + ".cpp"

    # mainRelPathのスラッシュの向きを/に統一
    includeMainPath = str(mainRelPath).replace("\\", "/")
    # テストファイルに書き込む文字列を作成
    testSource = f"""#include <gtest/gtest.h>
#include \"{includeMainPath}\"

TEST({sourceName}, {args.case})
{{
    EXPECT_TRUE(true);    // 成功
}}
"""
    print(testFilePath)
    # ファイルを作成
    # ディレクトリの存在チェック
    testDir = os.path.dirname(testFilePath)
    if testDir and not os.path.exists(testDir):
        os.makedirs(testDir)
    fileUtl.CreateFile(path = testFilePath, value = testSource)

    # ディレクトリを戻す
    os.chdir(cDir)

    # プロジェクトを更新
    proj.UpdateProject()

    if args.open:
        # テストファイルの絶対パスを求める
        fullTestFilePath = testDir + "/" + testFilePath
        # 作成したファイルを開く
        fileUtl.OpenFile(fullTestFilePath)
