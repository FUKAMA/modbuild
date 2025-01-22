
# 色の定義
#--------------------------------
import sys

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
SKY = "\033[96m"
RESET = "\033[0m"

# 赤文字でエラーメッセージを出力する
def Error(message,isExit = False):
    print(f"{RED}Error: {message}{RESET}")  
    if isExit:
        sys.exit(1)

# 黄文字で警告メッセージを出力する
def Warn(message):
    print(f"{YELLOW}Warning: {message}{RESET}")

# システムメッセージを出力
def SysMessage(message):
    print(f"{SKY}{message}{RESET}")


# 以降に出力される文字を引数のものに変化させる
def ChangeColor(color):
    print(f"{color}")

# 文字の色をデフォルトに戻す
def ColorSeset():
    print(f"{RESET}")

