import pkgutil
import importlib

def load_commands():
    """
    `commands` ディレクトリ内のすべてのモジュールを探索して動的にインポートする。
    """
    commands = {}
    # このパッケージの名前を取得
    package_name = __name__

    # このパッケージのすべてのモジュールを探索
    for loader, module_name, is_pkg in pkgutil.iter_modules(__path__):
        # モジュールを動的にインポート
        full_module_name = f"{package_name}.{module_name}"
        try:
            module = importlib.import_module(full_module_name)

            # モジュールが `add_subcommand` を定義している場合のみ登録
            if hasattr(module, "add_subcommand"):
                commands[module_name] = module
        except Exception as e:
            print(f"Error loading module {module_name}: {e}")
    return commands

