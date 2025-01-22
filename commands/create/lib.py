import subprocess
import os
import shutil
import zipfile
import json

from modules import proj
from modules import gitUtl
from modules.utl import log

import clitemp

# 説明や引き数などを登録する
def Register(subparsers):
    #=====================================
    # 引き数定義ゾーン開始
    #--------------
    # ↓ここにこのコマンドの説明を書く
    helpString = "静的ライブラリプロジェクトを作成"
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
    parser.add_argument("--name", required=True, help="ライブラリの名前")
    parser.add_argument("--type", choices=["STATIC", "SHARED"], default="STATIC", help="動的ライブラリか、静的ライブラリか")
    parser.add_argument("--open", choices=["private", "public"], default="private", help="リポジトリの公開設定")
    #--------------
    # 引き数定義ゾーン終了
    #=====================================


# コマンドを実行したときの処理
def Execute(args):

    # ライブラリの名前
    libName = args.name
    # ライブラリの公開設定
    openType = args.open

    # 既に引数の名前のリポジトリが存在していたら中断
    isCreatedResult = gitUtl.IsAlreadyCreatedRepo(libName)
    if isCreatedResult == True:
        log.Error("すでに同じ名前のリポジトリが存在します")
        return False
    elif not isCreatedResult == False:
        log.Error(f"{isCreatedResult}")
        return False


    
    # 空のリポジトリを作成しクローン、そこに移動
    log.SysMessage("リポジトリの作成開始")
    libDirPath = os.getcwd() + "/" + args.name + "/"
    os.mkdir(libDirPath)
    gitUtl.CreateRepo(libName, openType)
    os.chdir(libDirPath)
    log.SysMessage("リポジトリの作成完了")

    # 最低限必要なブランチを作成する
    gitUtl.CreateBranch("develop")
    gitUtl.CreateBranch("main")

    # ライブラリを作成
    log.SysMessage("ライブラリの作成開始")
    proj.CreateLib(libName,openType,args.type)
    log.SysMessage("ライブラリの作成完了")

    # ライブラリを更新
    proj.UpdateProject()

    # ディレクトリの内容をGitにプッシュ
    gitUtl.CommitAndPushDir(message="プロジェクトの初期化完了")

