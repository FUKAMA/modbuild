import subprocess
import os
import shutil
import requests
import zipfile
import json

from pathlib import Path

from modules.utl import log



# 引数のパスのディレクトリがプロジェクトとして機能するか調べる
def IsProject():

    # projDataファイルのフルパスを作成
    projDataName = "projData.json"
    projDataPath = os.getcwd() + "/" + projDataName

    # projDataファイルが存在すればtrueを返す
    if os.path.isfile(projDataPath):
        return True

    # 存在しなければfalseを返す
    return False
    

# ライブラリを作成するコマンド
def CreateLib(name,libType,openType):

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
        "ProjName": name,
        "LibType": libType,
        "OpenType": openType,
        "libraries" : {}
    }

    # JSONファイルに書き込む
    with open(proj_data_path, "w", encoding="utf-8") as projDataFile:
        json.dump(projData, projDataFile, indent=4, ensure_ascii=False)    
    # プロジェクトを初期化
    subprocess.run(["cmake",f"-DPROJ_NAME={name}",f"-DPROJ_TYPE={libType}"])

# プロジェクトを更新する
def UpdateProject():

    # 今いるディレクトリがプロジェクトとして機能してなければ中断
    if not IsProject():
        log.Error("プロジェクトディレクトリではありません")
        return False

    # mainディレクトリの中のインクルードファイルからプロジェクト名を取得
    files = os.listdir(os.getcwd()+"/main/include")
    projName = [i for i in files if i.endswith(".hpp") == True]
    subprocess.run(["cmake",f"-DPROJ_NAME={os.path.splitext(projName[0])[0]}","-DPROJ_TYPE=STATIC"])

# 今いるディレクトリのプロジェクトをビルドする
def BuildProject():
    # 今いるディレクトリがプロジェクトとして機能してなければ中断
    if not IsProject():
        log.Error("プロジェクトディレクトリではありません")
        return False

    cPath = os.getcwd() + "/CMakeLists.txt"
    cPathObj = Path(cPath)
    # 今いるディレクトリがプロジェクト出なければ中断
    if not cPathObj.is_file():
        log.Error("有効なプロジェクトディレクトリではありません")
        return False
    subprocess.run(["cmake","--build","."])
    return True

# 
def GetSlnPath():

    with open("projData.json", "r", encoding = "utf-8") as file:
        data = json.load(file)  # JSONをPythonの辞書型に変換
    projName = data.get("ProjName")

    slnFullPath = os.getcwd() + "/" + projName + ".sln"

    # ソリューションファイルが存在してなければ中止
    slnFullPathObj = Path(slnFullPath)
    if not slnFullPathObj.is_file():
        log.Error("ソリューションファイルが存在しません")
        return False

    return slnFullPath

