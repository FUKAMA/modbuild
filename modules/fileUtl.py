import os
from tkinter import Tk, filedialog
import sys
from pathlib import Path
from modules.utl import log

# エクスプローラーを開いてファイルを指定しそのパスを返す関数
# 拡張子の指定方法:extList = [("ヘッダファイル", "*.hpp"),("ソースファイル", "*.cpp")]
def GetFilePathFromExplorer(extList = [], currentDir = None, titleText = "ファイルを選択"):

    # プロジェクトのあるディレクトリを保存
    cDir = os.path.abspath(os.getcwd())
    # ディレクトリを選択
    fileDir = filedialog.askopenfilename(
        title = titleText,
        filetypes = extList,
        initialdir = currentDir
    )

    # パスが返ってこなかったら失敗
    if not fileDir:
        return None

    return fileDir


# エクスプローラーを開いてディレクトリを指定しそのパスを返す関数
def GetDirPathFromExplorer(currentDir = None):

    fileDir = filedialog.askdirectory(initialdir = currentDir)

    if not fileDir:
        return None
    
    return fileDir


def CreateFile(path,value,enco="utf-8-sig"):
    # ファイルに書き込む文字列を作成
    hFileString = f"#pragma once\n"
    cppFileString = ""
        # ファイルを作成
    with open(path,mode="w",encoding=enco) as file:
        file.write(value)

# ファイルをソリューションで起動する
def OpenFile(fullPath):
    # 引数のパスが存在するか調べる
    fullPathObj = Path(fullPath)
    if not fullPathObj.is_file():
        log.Error("存在しないパスは開けません")
        return
    # テストファイルの絶対パスを求める
    os.system(f"start {fullPath}")
