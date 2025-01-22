#==================================================
# モジュールのテストを実行するサブコマンド
#==================================================

import os
import subprocess
from tkinter import filedialog
from tkinter import Tk, filedialog
import json

import clitemp

helpString = "ソリューションを起動する"

def Register(subparsers):
    parser = clitemp.CreateCommandParser(__file__,subparsers, helpString)

def Execute(args):

    # proj_data_path = "projData.json"
    # json.load(proj_data_path)

    # open()   
    with open("projData.json", "r", encoding="utf-8") as file:
        data = json.load(file)  # JSONをPythonの辞書型に変換
    projName=data.get("ProjName")

    os.system(f"start {projName}.sln")


    # # ソリューションのパスを指定
    # solution_path = filedialog.askopenfilename(
    #     title="プロジェクトファイルを選択",
    #     filetypes=[("ソリューションファイル", "*.sln")]
    # )
    # print(solution_path)
    # dir_name=os.path.dirname(solution_path)
    # print(dir_name)

    # os.startfile(solution_path)

    # os.system(["cd","C:\Project\ECO Engine\ECO Engine"])

    # subprocess.run(["cd","C:\Project\ECO Engine\ECO Engine"],shell=True)