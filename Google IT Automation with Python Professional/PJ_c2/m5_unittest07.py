# Validation test: 入力値が正しい形式や範囲に合致しているかどうかを検証するテスト (=妥当性の確認)
# コードをテストして期待通りに動作することを検証すること(assertEqual)と、期待通りの場合に正しいエラーが発生すること(assertRaises)をテストすることが含まれる

#!/user/bin/env python3
import unittest

from validations validate_user

class TestValidateUser(unittest, TestCase):
  def test_valid(self):
    self.assertEqual(validate_user("validuser", 3), True)

  def test_too_short(self):
    self.assertEqual(validate_user("inv", 5), False)
  
  def test_invalid_characters(self):
    self.assertEqual(validate_user("invalid_user", 1), False)

  # 指定したエラーや例外が発生するかどうか確認
  def test_invalid_minlen(self):
    self.assertRaises(ValueError, validate_user, "user", -1)


unittest.main()
