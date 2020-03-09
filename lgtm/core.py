# main.pyから呼び出されている

import click
# コマンドラインツール作成ライブラリ
from lgtm.drawer import save_with_message
from lgtm.image_source import get_image


@click.command()
# コマンドとして実行したい関数につける
@click.option('--message', '-m', default='LGTM',
              show_default=True, help='画像に乗せる文字列')
# オプションで渡すものを指定
@click.argument('keyword')
# 位置引数で渡すものを指定
def cli(keyword, message):
    """LGTM画像生成ツール"""
    lgtm(keyword, message)
    click.echo('lgtm')  # 動作確認用


def lgtm(keyword, message):
    with get_image(keyword) as fp:
        save_with_message(fp, message)
