# How to use pytest

import pytest
class Fruit:
    def __init__(self, name):
        self.name = name
        self.cubed = False


    def cube(self):
        self.cubed = True


class FruitSalad:
    def __init__(self, *fruit_bowl):
        self.fruit = fruit_bowl
        self._cube_fruit()


    def _cube_fruit(self):
        for fruit in self.fruit:
            fruit.cube()

# Arrange Decorater
@pytest.fixture
def fruit_bowl():
    return [Fruit("apple"), Fruit("banana")]


def test_fruit_salad(fruit_bowl):
    # Act
    fruit_salad = FruitSalad(*fruit_bowl)



### unittestとpytestは何が違うのか
# どちらもpythonのテストフレームワークで、使用する場面によって使い分けたり開発者の好みで分けてよい。
# 後方互換(新バージョンに対応させるための互換性)があるため、unittestは大きな修正なしにpytestを使ってシームレスに実行可能。これにより、開発者はpytestを徐々に採用し、コードに統合することが可能。
# unittest:
# Pythonに標準搭載されているフレームワークでJavaなど他言語のUnix系のテストフレームワークと似た構造を持っている。
# クラスベースでTestCaseクラスを継承してテストメソッドを使用するため、コード量が少し多くなりがち。
# 専用のアサ―ションメソッドが多いため、リファレンスが必要になる。
# プラグイン複雑
# pytest:
# 関数ベースで簡潔にテストが書ける。設定不要、簡易インストール、テストコード短くなりやすく、デコレ―タを使用した柔軟なテストが可能。
# プラグイン容易、コードカバレッジの測定やパラメータ化、テスト並走実行など簡単に拡張可能、特定のプラグインで追加機能を得られるため、大規模なプロジェクトにも対応が可能。
# python標準のassert文がそのまま使用可能なので、エラーメッセージが自動生成されてシンプルにコードを記述可能。テスト結果が失敗した場合、詳細なデバッグ情報が表示されて便利そう。
# コマンドラインでテストファイルや関数名を指定するだけで特定のテストを実行することができる。
