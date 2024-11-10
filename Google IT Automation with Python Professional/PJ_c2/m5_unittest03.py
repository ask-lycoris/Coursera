# Batch test: 複数のテストケースをまとめて処理する
import unittest
from rearrange import rearrange_name

class TestRearrange(unittest.TestCase):
    
    def test_multiple_cases(self):
      # 他のテストケースを追加
        test_cases = [
            ("Lovelace, Ada", "Ada Lovelace"),
            ("Einstein, Albert", "Albert Einstein"),
            ("Curie, Marie", "Marie Curie")]
        ]
        
        for name, expected in test_cases:
          # self.subTest() を使用することで各テストケースが独立して実行され、失敗した場合でも他のてすとけーすの結果が影響を受けないようにすることが可能
            with self.subTest(name=name):
                self.assertEqual(rearrange_name(name), expected)

unittest.main()

### テストの粒度
# unit test/component test: 最も細かい粒度のテスト。個々の関数やメソッドは、さまざまな入力に対して期待される出力を返すかどうか(正しく動作するか)を確認する。
# integration test:複数のユニットが組み合わさったときに正しく動作するかを確認する、例えば、データベースとのやり取りや外部APIとの連携をテストする。
# system test: アプリケーション全体が要件を満たしているかを総合的に確認する。ユーザの観点から機能をテストする。
# user acceptance Test: 最終的なユーザやクライアントがアプリケーションを受け入れるためのテスト。ビジネス要件が満たされているかを確認する。
# ※ 基本的にはユニットテストをしっかりと行い、必要に応じて統合テストやシステムテストを行うことでバランスの取れたテスト戦略を構築することが可能。

### テストケースの設計
# 正常系テスト: 正常な入力に対して期待される出力を確認する。基本的なテストであり、必ず行うべき。
# 異常系テスト: 異常な入力（無効なデータやエッジケース）に対して、アプリケーションが適切にエラーハンドリングを行うかを確認。
# 境界値テスト: rangeの境界に近い値（例えば、リストの最初や最後の要素、最大値や最小値など）をテストする。これにより、オフバイワンエラー（1つずれたエラー）を検出しやすくなる。
# ※ 過剰なテストは避け、重要な機能や頻繁に更新変更される部分を優先して作成する。コードカバレッジは70-80%を目指すことが一般的ではあるが、高いカバレッジが高い品質を示すとは限らない。
#    テストケースもメンテナンスが必要なため、テストケースは明確にしておくべき。

