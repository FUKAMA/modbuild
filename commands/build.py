#==================================================
# モジュールのビルドを実行するサブコマンド
#==================================================

def Register(subparsers):
    parser = subparsers.add_parser("build", help="モジュールをビルドする")

    
def Execute(args):
    print("ビルド実行")

