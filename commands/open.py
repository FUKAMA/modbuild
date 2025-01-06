#==================================================
# モジュールのテストを実行するサブコマンド
#==================================================

import os
import subprocess
from tkinter import filedialog
from tkinter import Tk, filedialog

def Register(subparsers):
    parser = subparsers.add_parser("open", help="モジュールの開発環境を開く")

def Execute(args):

    # ソリューションのパスを指定
    solution_path = filedialog.askopenfilename(
        title="プロジェクトファイルを選択",
        filetypes=[("ソリューションファイル", "*.sln")]
    )
    print(solution_path)
    dir_name=os.path.dirname(solution_path)
    print(dir_name)

    # os.startfile(solution_path)

    # os.system(["cd","C:\Project\ECO Engine\ECO Engine"])

    # subprocess.run(["cd","C:\Project\ECO Engine\ECO Engine"],shell=True)