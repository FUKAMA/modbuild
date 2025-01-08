#==================================================
# モジュールを更新するコマンド
#==================================================

import subprocess
import os
import fnmatch

def Register(subparsers):
    parser = subparsers.add_parser("update", help="モジュールを更新する")

def Execute(args):
    nowDir=os.path.basename(os.getcwd())
    print(nowDir)

    # mainディレクトリの中のインクルードファイルからプロジェクト名を取得
    files = os.listdir(os.getcwd()+"/main/include")
    projName = [i for i in files if i.endswith(".hpp") == True]
    subprocess.run(["cmake",f"-DPROJ_NAME={os.path.splitext(projName[0])[0]}","-DPROJ_TYPE=STATIC"])
