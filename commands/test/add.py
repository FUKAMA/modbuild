import os
import subprocess
from tkinter import Tk, filedialog
from pathlib import Path
import sys

import clitemp

# 説明や引き数などを登録する
def Register(subparsers):
    #=====================================
    # 引き数定義ゾーン開始
    #--------------
    # ↓ここにこのコマンドの説明を書く
    helpString = "特定のファイルのテストを追加する"
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
    parser.add_argument("--name", help="テスト名")
    #--------------
    # 引き数定義ゾーン終了
    #=====================================

# コマンドを実行したときの処理
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

    if not fileDir:
        print("有効なファイルを指定してください")
        sys.exit(1)

    fileObj = Path(fileDir).resolve()

    # テストを作成するソースファイルの名前
    sourceName =os.path.splitext(os.path.basename(fileDir))[0]

    # mainのsrcまで移動
    os.chdir("main/src")
    # srcからの相対パスを求める
    mainRelPath = fileObj.relative_to(os.getcwd())

    # testのsrcまで移動
    os.chdir(cDir)
    os.chdir("test/src")
    # 相対パスを使いtestのsrcからの絶対パスを作成
    testPath = os.getcwd() + f"/{mainRelPath}"

    testDir = os.path.dirname(testPath)

    os.mkdir(testDir)

    # ディレクトリを移動
    os.chdir(testDir)

    testFileName = sourceName + "_" + args.name

    # テストファイルに書き込む文字列を作成

    testSource = f"#include <gtest/gtest.h>\n\
#include \"{mainRelPath}\"\n\
TEST({sourceName}, {args.name})\n\
{{\n\
    EXPECT_TRUE(true);    // 成功\n\
}}\n\
"

    # ファイルを作成
    with open(f"{testFileName}.cpp",mode="w") as file:
        file.write(testSource)

    # ディレクトリを戻す
    os.chdir(cDir)

    # プロジェクトを更新
    files = os.listdir(os.getcwd()+"/main/include")
    projName = [i for i in files if i.endswith(".hpp") == True]
    subprocess.run(["cmake",f"-DPROJ_NAME={os.path.splitext(projName[0])[0]}","-DPROJ_TYPE=STATIC"])
