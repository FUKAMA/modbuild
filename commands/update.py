#==================================================
# モジュールを更新するコマンド
#==================================================

import subprocess
import os

def Register(subparsers):
    parser = subparsers.add_parser("update", help="モジュールを更新する")

def Execute(args):
    nowDir=os.path.basename(os.getcwd())
    print(nowDir)
    subprocess.run(["cmake",f"-DPROJ_NAME={nowDir}","-DPROJ_TYPE=STATIC"])
