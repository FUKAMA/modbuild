import os
import subprocess
from tkinter import Tk, filedialog
import sys
from pathlib import Path
from modules.utl import log
from modules import proj

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

# # ファイルをソリューションで起動する
# def OpenFile(fullPath):
#     # 引数のパスが存在するか調べる
#     fullPathObj = Path(fullPath)
#     if not fullPathObj.is_file():
#         log.Error("存在しないパスは開けません")
#         return False
#     # テストファイルの絶対パスを求める
#     # subprocess.run(["start",f"{fullPath}"])
#     os.system(f"start {fullPath}")

#     return True


# ファイルをソリューションで起動する
# ToDo:VS2022専用の実装でなくする
def OpenFile(fullPath):
    
    # ソリューションのパスを求める
    slnPath = proj.GetSlnPath()
    if not slnPath:
        return False
    
    # 引数のパスが存在するか調べる
    slnPathObj = Path(slnPath)
    if not slnPathObj.is_file():
        log.Error("存在しないソリューションは開けません")
        return False
    
    fullPathObj = Path(fullPath)
    if not fullPathObj.is_file():
        log.Error("存在しないファイルは開けません")
        return False
    
    # ファイルをソリューションで開く
    subprocess.run(
        [
            "C:/Program Files/Microsoft Visual Studio/2022/Community/Common7/IDE/devenv.exe",
            "/Edit",
            f"{slnPath}",
            f"{fullPath}"
        ],
        check = True
    )

    return True
