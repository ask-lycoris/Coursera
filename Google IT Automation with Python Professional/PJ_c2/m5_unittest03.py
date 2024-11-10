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

