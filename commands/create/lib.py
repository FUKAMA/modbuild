import subprocess
import os
import shutil
import requests
import zipfile
import json

from modules.proj import createLib

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
    commName =os.path.splitext(os.path.basename(os.path.abspath(__file__)))[0] 
    parser = subparsers.add_parser(f"{commName}", help=f"cmm: {helpString}")
    
    
    #=====================================
    # 引き数定義ゾーン開始
    #--------------
    # parser.add_argument("--変数名", help="変数の説明")
    #--------------
    parser.add_argument("--name", required=True, help="ライブラリの名前")
    # parser.add_argument("--type", choices=["STATIC", "SHARED"], default="STATIC", help="動的ライブラリか、静的ライブラリか")
    parser.add_argument("--type", choices=["private", "public"], default="private", help="リポジトリの公開設定")
    #--------------
    # 引き数定義ゾーン終了
    #=====================================


# コマンドを実行したときの処理
def Execute(args):

    createLib.CreateLib(args.name,args.type)

    # # GitHubのリポジトリを作成
    # subprocess.run(["gh","repo","create",f"{args.name}",f"--{args.type}"])
    # # GitHubのユーザー名を取得
    # result = subprocess.run(
    #     ["gh", "api", "user", "--jq", ".login"],
    #     stdout=subprocess.PIPE,
    #     stderr=subprocess.PIPE,
    #     text=True,
    #     check=True
    # )
    # username = result.stdout.strip()
    # # 作成したリポジトリをクローン
    # subprocess.run(["git","clone",f"https://github.com/{username}/{args.name}.git"])
    # # クローンしたディレクトリに移動
    # os.chdir(f"{args.name}")


    # # モジュールテンプレートをダウンロード
    # template_url = "https://github.com/FUKAMA/TempModule/archive/refs/heads/main.zip"
    # template_zip = "TempMod.zip"
    # print(f"Downloading template from {template_url}...")
    # response = requests.get(template_url)
    # with open(template_zip, "wb") as f:
    #     f.write(response.content)
    # print(f"Downloaded template to {template_zip}.")

    # # ダウンロードしたZIPを解凍
    # with zipfile.ZipFile(template_zip, 'r') as zip_ref:
    #     zip_ref.extractall("TempModule-main")

    # # 解凍したテンプレートの中身を移動
    # temp_dir = "TempModule-main/TempModule-main"
    # for item in os.listdir(temp_dir):
    #     shutil.move(os.path.join(temp_dir, item), ".")

    # # 展開に使ったディレクトリとZIPファイルを削除
    # shutil.rmtree("TempModule-main")
    # os.remove(template_zip)

    # # プロジェクト名などをJsonに保存
    # #-------------------------------------

    # # JSONファイルのパス
    # proj_data_path = "projData.json"

    # # 書き込むデータを作成
    # projData = {
    #     "ProjName": args.name,
    #     "ProjType": args.type,
    #     "libraries" : {}
    # }

    # # JSONファイルに書き込む
    # with open(proj_data_path, "w", encoding="utf-8") as projDataFile:
    #     json.dump(projData, projDataFile, indent=4, ensure_ascii=False)    # プロジェクトを初期化
    # subprocess.run(["cmake",f"-DPROJ_NAME={args.name}",f"-DPROJ_TYPE={args.type}"])


    # # 初期コミットとプッシュ
    # subprocess.run(["git", "add", "."], check=True)
    # subprocess.run(["git", "commit", "-m", "Initial commit"], check=True)
    # subprocess.run(["git", "branch", "-M", "main"], check=True)
    # subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
