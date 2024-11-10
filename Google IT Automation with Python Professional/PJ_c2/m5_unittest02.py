# ネーミングの慣習は、「<対象となる関数>_test」とする。

# sample code「rearrange.py」

#!/usr/bin/env python3
import re

def rearrange_name(name):
  result = re.search(r"^([\w .]*), ([\w .]*)$", name)
  return "{} {}".format(result[2], result[1])


# unittest「rearrange_test.py」

#!/usr/bin/env python3
import unittest
from rearrange import rearrange_name

# 各テストクラス名は Test で始めること。クラスで定義したプレフィックス Test... で始まるメソッドはすべて自動的にテストフレームワークで実行できるテストとなる。
class TestRearrange(unittest.TestCase):
    
  def test_basic(self):
    testcase = "Lovelace, Ada"
    expected = "Ada Lovelace"
  # 継承したテストケースクラスから提供されたassertEqualメソッドを使用
    self.assertEqual(rearrange_name(testcase), expected)

# Run the tests
# Entry point for conducting tests
unittest.main()
# 上記のように呼び出すことで、スクリプト内で定義されたすべてのテストメソッドを自動的に探し、実行するように組まれている。
