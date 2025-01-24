import os
import sys

import clitemp
from modules import proj

# 説明や引き数などを登録する
def Register(subparsers):
    #=====================================
    # 引き数定義ゾーン開始
    #--------------
    # ↓ここにこのコマンドの説明を書く
    helpString = "プロジェクトをビルドする"
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

    #--------------
    # 引き数定義ゾーン終了
    #=====================================

# コマンドを実行したときの処理
def Execute(args):
    proj.BuildProject()
