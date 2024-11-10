import unittest
import os
import shutil

# Target function for test
def simple_addition(a, b):
	return a + b

# Paths for file operations
ORIGINAL_FILE_PATH = "/tmp/original_test_file.txt"    # テスト結果を書き込む一次ファイル
COPIED_FILE_PATH = "/mnt/data/copied_test_file.txt"   # テスト結果をコピーする先
# Global counter: テストの実行回数をカウントする
COUNTER = 0

# This method is a special method for unittest framework which will be run once [before] any tests or test classes.
# クラスのインスタンスに依存しないため、selfを引数にとらない。
# モジュール内のすべてのテストケースに共通する初期設定を行うために使用される
def setUpModule():   # 
	global COUNTER
	COUNTER = 0
    
	# Create a file in /tmp
	with open(ORIGINAL_FILE_PATH, 'w') as file:
    	file.write("Test Results:\n")

# This method This method is a special method for unittest framework which will be run once [after] all tests and test classes.
# クラスのインスタンスに依存しないため、selfを引数にとらない。
# テストの後処理を行うために使用される
def tearDownModule():
	# Copy the file to another directory
	shutil.copy2(ORIGINAL_FILE_PATH, COPIED_FILE_PATH)

# Remove the original file
	os.remove(ORIGINAL_FILE_PATH)

# テストケースの列挙
class TestSimpleAddition(unittest.TestCase):
	# This method will be run before each individual test. The 'self' argument is needed duo to use class instance.
	def setUp(self):
    	global COUNTER
    	COUNTER += 1
	# This method will be run before each individual test. The 'self' argument is needed duo to use class instance.
	def tearDown(self):
    	# Append the test result to the file
    	with open(ORIGINAL_FILE_PATH, 'a') as file:
        	result = "PASSED" if self._outcome.success else "FAILED"
        	file.write(f"Test {COUNTER}: {result}\n")

	def test_add_positive_numbers(self):
    	self.assertEqual(simple_addition(3, 4), 7)

	def test_add_negative_numbers(self):
    	self.assertEqual(simple_addition(-3, -4), -7)

# Running the tests
# テストケースを自動的に見つけてロードする機能
# 指定したテストクラスからテストメソッドを全て見つけてテストスイート(複数のテストをまとめて実行するためのオブジェクト)を作成する機能
suite = unittest.TestLoader().loadTestsFromTestCase(TestSimpleAddition)
# テストを実行し、その結果をコンソールに出力するためのテストランナーをhuman readableに作成する機能
runner = unittest.TextTestRunner()
# Execute test suite by using test runner
runner.run(suite)

# Read the copied file to show the results
with open(COPIED_FILE_PATH, 'r') as result_file:
	test_results = result_file.read()

print(test_results)
