import subprocess
import os
import sys



# 説明や引き数などを登録する
def Register(subparsers):
    #=====================================
    # 引き数定義ゾーン開始
    #--------------
    # ↓ここにこのコマンドの説明を書く
    helpString = "プロジェクトを更新する"
    #--------------
    # 引き数定義ゾーン終了
    #=====================================
    
    # コマンド名をファイル名から取得
    commName =os.path.splitext(os.path.basename(os.path.abspath(__file__)))[0] 
    parser = subparsers.add_parser(f"{commName}", help=f"cmm: {helpString}")
    
    
    #=====================================
    # 引き数定義ゾーン開始
    #--------------
    # parser.add_argument("--変数名", help="変数の説明")
    #--------------
    parser.add_argument("--hoge",default="aaa", help="HOGEるかどうか")
    #--------------
    # 引き数定義ゾーン終了
    #=====================================

# コマンドを実行したときの処理
def Execute(args):
    nowDir=os.path.basename(os.getcwd())
    print(nowDir)

    # mainディレクトリの中のインクルードファイルからプロジェクト名を取得
    files = os.listdir(os.getcwd()+"/main/include")
    projName = [i for i in files if i.endswith(".hpp") == True]
    subprocess.run(["cmake",f"-DPROJ_NAME={os.path.splitext(projName[0])[0]}","-DPROJ_TYPE=STATIC"])
