# The name of test scripts should be 「<target function>_test」 by convention.

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

# The name of class should be Test..., prefix. All methods begin with Test will be executed automatically in test framework.
class TestRearrange(unittest.TestCase):
# 対象関数の基本的な挙動確認テスト
  def test_basic(self):
    testcase = "Lovelace, Ada"
    expected = "Ada Lovelace"
  # 継承したテストケースクラスから提供されたassertEqualメソッドを使用
    self.assertEqual(rearrange_name(testcase), expected)

# Edge cases: Inputs to ourcode that produce unexpected results, and found at the extreme ends of the ranges of input we image our programs will typically work with.
# 予期しない結果をもたらすコードへの入力
　def test_empty(self):
    testcase = ""
    expected = ""
    self.assertEqual(rearrange_name(test_case), expected)   # NameError

# Additional Test Cases: Create other test cases with your imagination.
def test_double_name(self):
    testcase = "Hopper, Grace M."
    expected = "Grace M. Hopper"
    self.assertEqual(rearrange_name(testcase), expected)

def test_one_name(self):
    testcase = "Voltaire"
    expected = "Voltaire"
    self.assertEqual(rearrange_name(testcase), expected)   # AssertionError
  
# イメージは、関数をつくりながら、その関数がどんな結果をもたらすかのテストコードを書いてチェックしながら目的の関数が出来上がるまでバグやエラーハンドリングを追加する等修正し続ける、そんな感じ
# なお、修正する箇所はなるべく少ない方が良いので、複数のエラーの原因を作っている箇所を特定し問題を集約して最適解を修正として盛り込むのがベスト！
                     
# Run the tests
# Entry point for conducting tests
unittest.main()
# 上記のように呼び出すことで、スクリプト内で定義されたすべてのテストメソッドを自動的に探し、実行するように組まれている。
