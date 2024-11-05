# ref[https://docs.python.org/3/library/os.path.html]
# File paths have 2 types, relative path and absolute path. Python programmers tend to avoiding the absolute path.
# File paths are most often used to save and load information.
# Programmers use command OS path to wrap the directories to avoid the difference between platform.
# Most errors relates to the confusion of where the scripts calling the function and where python function calls.
# んー。なんかエラー出るな。

# Create a directory and move a file from one directory to another using low-level OS functions.
import os
# Python標準ライブラリで古くから存在するため、互換性が高い。パスを文字列として扱っている。
# ファイルやディレクトリの操作に対して関数ベースのUIを提供するが、やや直感的でない。

# Check to see if a directory named "test1" exists under the current
# directory. If not, create it:
dest_dir = os.path.join(os.getcwd(), "test1")
if not os.path.exists(dest_dir):
  os.mkdir(dest_dir)

# Construct source and destination paths:
# os.path.join(): It creates a string containing cross-platform concatenated directories.
# そう！そのOSに依存したファイルパスで読みに行ってくれる関数なので、異なるプラットフォームでも連結可能な点が便利！
src_file = os.path.join(os.getcwd(), "website", "README.md")
dest_file = os.path.join(os.getcwd(), "test1", "README.md")

# Move the file from its original location to the destination:
if os.path.exists(dest_file):
    # Move the file from its original location to the destination:
    os.rename(src_file, dest_file)
    print(f'Moved {dest_file} to {src_file}')
else:
    print(f'Error: {dest_file} does not exist.')

# Create a directory and move a file from one directory to another using Pathlib, high-level OS function.
from pathlib import Path
# Python3.4以降でのみ使用可能。パスをオブジェクトとして扱っている。
# OOP指向のUIを持ち、'Path' objectを使用してfile pathを表現するため、パス操作が直感的でメソッドを利用して記述可能。

# Check to see if the "test1" subdirectory exists. If not, create it:
dest_dir = Path("./test1/")
if not dest_dir.exists():
  dest_dir.mkdir()

# Construct source and destination paths:
src_file = Path("./website/README.md")
dest_file = dest_dir / "NOTREADME.md"

if src_file.exists():
    # Move the file from its original location to the destination:
    src_file.rename(dest_file)
    print(f'Moved {src_file} to {dest_file}')
else:
    print(f'Error: {src_file} does not exist.')
