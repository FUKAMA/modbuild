import os
import sys
import json
import subprocess

import clitemp
from modules.utl import log
from modules import proj

# 説明や引き数などを登録する
def Register(subparsers):
    #=====================================
    # 引き数定義ゾーン開始
    #--------------
    # ↓ここにこのコマンドの説明を書く
    helpString = "自作のモジュールをダウンロードしてリンクする"
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
    parser.add_argument(
        "--path",
        help=
        "リンクするモジュールのGitパス \
        FetchContentで使用できるパス"
    )

    parser.add_argument("--name",help="リンクするモジュールの名前")
    #--------------
    # 引き数定義ゾーン終了
    #=====================================

# コマンドを実行したときの処理
def Execute(args):

    if not proj.IsProject():
        log.Error("プロジェクトディレクトリではありません")
        return False
    
    isArgs = True
    if not args.name:
        log.Error("モジュールの名前を指定してください")
        isArgs = False    
    if not args.path:
        log.Error("Gitパスを指定してください")
        isArgs = False
    if not isArgs:
        return False

    exePath = os.getcwd()
    os.chdir(exePath)

    proj_data_path = "projData.json"

    fullProjPath = exePath + "/" + proj_data_path

    # projData.jsonを読み込む
    pjFile = open(fullProjPath, "r")
    if not pjFile:
        log.Error("ファイルが存在しません")
        return False
    pjData = json.load(pjFile)


    modItems = pjData.get("modules",[])

    isLinked = False
    # 既にリンクしてるか確認する
    isLinked = any(item["path"] == args.path for item in modItems)

    # 既にリンクしてたら終了
    if isLinked == True:
        log.Error("既にリンク済みのモジュールです")
        return False

    # リンクをリストに追加
    modItems.append({"path": f"{args.path}","name": f"{args.name}"})

    pjData["modules"] = modItems

    pjFileW = open(fullProjPath, "w")
    json.dump(pjData, pjFileW, indent=4, ensure_ascii=False)



    
    # mainディレクトリの中のインクルードファイルからプロジェクト名を取得
    files = os.listdir(os.getcwd()+"/main/include")
    projName = [i for i in files if i.endswith(".hpp") == True]
    subprocess.run(["cmake",f"-DPROJ_NAME={os.path.splitext(projName[0])[0]}","-DPROJ_TYPE=STATIC"])
