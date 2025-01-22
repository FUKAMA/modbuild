import subprocess
import os

from modules.utl import log

# 引数の名前のリポジトリが既に存在するか調べる
def IsAlreadyCreatedRepo(name):

    result = False

    # 結果が帰ってきたら存在する
    try:
        clRes = subprocess.run(
            ["gh","repo","view",f"{name}"],
            check=True,
            text=True,
            capture_output=True
        )

        result = True

    except subprocess.CalledProcessError as e:

        # エラーメッセージの内容が「リポジトリが存在しない」だった場合のみ結果にFalseを返す
        if "Could not resolve to a Repository" in e.stderr:
            result = False
        else:
            result = e.stderr

    return result

# 空のリポジトリを作成してクローン
def CreateRepo(name,openType):
    
    # GitHubのリポジトリを作成
    subprocess.run(["gh","repo","create",f"{name}",f"--{openType}"])
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
    subprocess.run(["git","clone",f"https://github.com/{username}/{name}.git"])


# コミットしてない変更がないか調べる
def HasUnCommitedChange():
    result = subprocess.run(["git","status","--porcelain"],check=True,text=True,capture_output=True)
    output = result.stdout.strip()

    # 変更があるか返す
    if output:
        return True
    return False


# ブランチを作成して移動する
def CreateBranch(branchName,parentBranch=None):

    # コミットしてない変更があれば中断
    if HasUnCommitedChange():
        log.Error("コミットしてない変更があります")
        return False

    # ブランチのフルネームを作成
    fullBranchName=branchName
    if parentBranch:
        fullBranchName = parentBranch+"/"+branchName
    
    # ブランチを作成して移動
    subprocess.run(["git", "switch", "-c",f"{fullBranchName}"],check=True)

    return True



# ブランチを移動する
def ChangeBranch(branchName):
    # コミットしてない変更が残ってたら中止する
    if HasUnCommitedChange():
        return

    # ブランチを移動
    subprocess.run(["git","switch",f"{branchName}"])


# 特定のディレクトリ以下にあるファイルをすべて今いるブランチにコミットしてプッシュする
def CommitAndPushDir(message,dir="."):

    # 引数のディレクトリ以下にある全てのファイルをステージに移動
    subprocess.run(["git", "add", f"{dir}"], check=True)
    # ステージの内容をコミット
    subprocess.run(["git", "commit", "-m", f"{message}"], check=True)
    # コミットをすべてプッシュする
    subprocess.run(["git", "push"], check=True)
