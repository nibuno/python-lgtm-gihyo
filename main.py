from lgtm import core


if __name__ == '__main__':
    core.cli()
"""
if __name__ == '__main__': ブロックについて
モジュール（コードを記述した.pyファイル）をスクリプトとして利用したい場合に記述する
Pythonのイディオム（慣用句）

Pythonが暗黙的に定義している変数の__name__によって結果が決まる
あるモジュールがpython(3)コマンドに渡された時、
モジュール内の変数__name__の値は__main__になる。

P151
"""

