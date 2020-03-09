import requests
# HTTPクライアントライブラリ
# HTTPリソースを簡単に利用するためのパッケージ
from io import BytesIO
from pathlib import Path


class LocalImage:
    """ファイルから画像を取得する"""

    def __init__(self, path):
        self._path = path
        # __init__(): インスタンスの初期化を行う特殊メソッド
        # 第一引数にインスタンス自身が渡ってくる
        # ここでインスタンスに属性を追加すると、このクラスのすべてのインスタンスがその属性を持つことになる

        # P128-129

    def get_image(self):
        return open(self._path, 'rb')
        # get_image()を呼び出すと画像のファイルオブジェクトを返す
        # 今回画像の取得で利用するすべてのクラスでこのメソッドを呼び出すと
        # 画像のファイルオブジェクトを返すようにする

        # open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
        # fileを開き、対応するファイルオブジェクトを返す
        # r: 読み込み用に開く（デフォルト）
        # b: バイナリモード
        # https://docs.python.org/ja/3/library/functions.html#open


class RemoteImage:
    """URLから画像を取得する"""

    def __init__(self, path):
        self._url = path
        # LocalImageクラスの__init__()と同じ

    def get_image(self):
        data = requests.get(self._url)
        # バイトデータをファイルオブジェクトに変換
        return BytesIO(data.content)


class _LoremFlickr(RemoteImage):
    # クラス定義名の後に(基底クラス名)をつけると基底クラスの性質を継承したサブクラスを定義できる
    # クラスの継承という
    # RemoteImageのメソッドをそのまま利用しつつ新しいメソッドや変数を追加、上書きできる。
    # _の作法ってなに？
    """キーワード検索で画像を取得する"""

    LOREM_FLICKER_URL = 'https://loremflickr.com'
    WIDTH = 800
    HEIGHT = 600
    # ex: https://loremflickr.com/WIDTH/HEIGHT/KEYWORD
    # にアクセスすると、指定サイズ・キーワードに沿ったランダムな画像を返してくれる

    def __init__(self, keyword):
        super().__init__(self._build_url(keyword))
        # super(): 基底クラスのメソッドを呼び出す
        # これで返されるオブジェクトはプロキシオブジェクトでありクラスオブジェクトそのものではない
        # 今回の場合、RemoteImageの__init__()メソッドを呼び出している

        # P140

    def _build_url(self, keyword):
        return (f'{self.LOREM_FLICKER_URL}/'
                f'{self.WIDTH}/{self.HEIGHT}/{keyword}'
                # fで始まっているのはf-string: 式を埋め込める文字列リテラル
                # 文字列中に{}でくくった変数や式を記述すると、実行時に{}が評価され、その結果に置き換えられる

                # P76
                )


KeywordImage = _LoremFlickr
# 内部用にLomenFlickrを利用していることがわかるように
# _LomenFlickr クラスを定義してKeywordImageという別名で参照できるように
# メリットとして、LomenFlickrから別のサービスを利用する際に
# クラスを差し替えるだけで済むようになる点が挙げられる


# コンストラクタとして利用するため
# 単語を大文字始まりにしてクラスのように見せる
def ImageSource(keyword):
    """最適なイメージソースクラスを返す"""
    if keyword.startswith(('http://', 'https://')):
        # http://またはhttps://で始まるならTrue
        # https://docs.python.org/ja/3/library/stdtypes.html?highlight=startswith#str.startswith
        return RemoteImage(keyword)
    elif Path(keyword).exists():
        return LocalImage(keyword)
    else:
        return KeywordImage(keyword)


def get_image(keyword):
    """画像のファイルオブジェクトを返す"""
    return ImageSource(keyword).get_image()
    # get_image()でImageSource()メソッドを利用することにより
    # クラスのように見せる

