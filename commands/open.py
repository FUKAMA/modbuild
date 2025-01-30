#==================================================
# モジュールのテストを実行するサブコマンド
#==================================================

import os
import subprocess
from tkinter import filedialog
from tkinter import Tk, filedialog
import json

import clitemp
from modules import proj
from modules.utl import log

helpString = "ソリューションを起動する"

def Register(subparsers):
    parser = clitemp.CreateCommandParser(__file__,subparsers, helpString)

def Execute(args):

    if not proj.IsProject():
        log.Error("プロジェクトディレクトリではありません")
        return False

    with open("projData.json", "r", encoding = "utf-8") as file:
        data = json.load(file)  # JSONをPythonの辞書型に変換
    projName = data.get("ProjName")

    os.system(f"start {projName}.sln")

    return True

