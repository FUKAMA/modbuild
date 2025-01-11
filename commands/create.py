#==================================================
# 新規モジュールの開発環境を構築するサブコマンド
#==================================================

import subprocess
import os
import shutil
import requests
import zipfile
import json

def Register(subparsers):
    parser = subparsers.add_parser("create", help="モジュールの開発環境を作成する")
    parser.add_argument("--name", required=True, help="プロジェクトの名前")
    parser.add_argument("--type", choices=["STATIC", "SHARED"], default="STATIC", help="プロジェクトの種類")

def Execute(args):



    # GitHubのリポジトリを作成
    subprocess.run(["gh","repo","create",f"{args.name}",f"--public"])
    # GitHubのユーザー名を取得
    result = subprocess.run(
        ["gh", "api", "user", "--jq", ".login"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=True
    )
    username = result.stdout.strip()
    # 作成したリポジトリをクローン
    subprocess.run(["git","clone",f"https://github.com/{username}/{args.name}.git"])
    # クローンしたディレクトリに移動
    os.chdir(f"{args.name}")


    # モジュールテンプレートをダウンロード
    template_url = "https://github.com/FUKAMA/TempModule/archive/refs/heads/main.zip"
    template_zip = "TempMod.zip"
    print(f"Downloading template from {template_url}...")
    response = requests.get(template_url)
    with open(template_zip, "wb") as f:
        f.write(response.content)
    print(f"Downloaded template to {template_zip}.")

    # ダウンロードしたZIPを解凍
    with zipfile.ZipFile(template_zip, 'r') as zip_ref:
        zip_ref.extractall("TempModule-main")

    # 解凍したテンプレートの中身を移動
    temp_dir = "TempModule-main/TempModule-main"
    for item in os.listdir(temp_dir):
        shutil.move(os.path.join(temp_dir, item), ".")

    # 展開に使ったディレクトリとZIPファイルを削除
    shutil.rmtree("TempModule-main")
    os.remove(template_zip)

    # プロジェクト名などをJsonに保存
    #-------------------------------------

    # JSONファイルのパス
    proj_data_path = "projData.json"

    # 書き込むデータを作成
    projData = {
        "ProjName": args.name,
        "ProjType": args.type
    }

    # JSONファイルに書き込む
    with open(proj_data_path, "w", encoding="utf-8") as projDataFile:
        json.dump(projData, projDataFile, indent=4, ensure_ascii=False)    # プロジェクトを初期化
    subprocess.run(["cmake",f"-DPROJ_NAME={args.name}",f"-DPROJ_TYPE={args.type}"])


    # 初期コミットとプッシュ
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "Initial commit"], check=True)
    subprocess.run(["git", "branch", "-M", "main"], check=True)
    subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
