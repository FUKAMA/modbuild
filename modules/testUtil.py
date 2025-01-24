import os
from modules.utl import log
from pathlib import Path

# 今のディレクトリに存在しているテストを実行する
def RunTest(case,name):
    testPathObj = Path(os.getcwd()+"/test.exe")
    if not testPathObj.is_file():
        log.Error("テスト実行ファイルが見つかりません")
        return False
    os.system(f"test.exe --gtest_filter={case}.{name}")

    return True
