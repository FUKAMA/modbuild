import os
import sys

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
    if not args.hoge:
        print("hogeが指定されてません")
        sys.exit(1)

    print(f"コマンドを実行: {args.hoge}")