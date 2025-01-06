#==================================================
# サブコマンドを作成する際にベースとなる形式が記述されているファイル
#==================================================

def Register(subparsers):
    parser = subparsers.add_parser("hogeComm", help="hogehoge説明文")
    parser.add_argument("--hogeArg", required=True, help="引数の定義")

def Execute(args):
    print(f"Building project: {args.name}, type: {args.type}")