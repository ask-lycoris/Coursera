### diff commnad：ファイルやディレクトリツリーごとの変更差分を特定し、保持および適用するコマンド

diff -u disk_usage_original.py disk_usage_fixed.py > disk_usage.diff
# -u option: unified format での出力を指定。変更された行の前後の行も含めて表示する。変更の前後の文脈が分かりやすくなる。
cat disk_usage.diff

# output
# --- disk_usage_original.py	2019-06-22 15:13:38.591579963 -0700

# +++ disk_usage_fixed.py	2019-06-22 15:41:35.013023839 -0700

# @@ -1,6 +1,7 @@

# + 追加された行
# - 削除された行   のような形で出力される

# その他の拡張機能を持った便利なdiff系コマンド
# diff -y: 2つのファイルの内容を横に並べて比較可能。
# vimdiff: Vim エディタを使用して、2つまたは3つのファイルを並べて表示し、差分を視覚的に確認可能。色分けされているため、変更点が明確。
# meld: GUI ベースの差分ツールで、ファイルやディレクトリの比較が可能。変更点を視覚的に表示し、マージ機能も備えている。
# kdiff3: 3つのファイルを同時に比較できるGUIツール。変更点を視覚的に確認し、マージも実行可能。

import difflib

# sampleA.txt を作成
with open('sampleA.txt', 'w') as f:
    f.write("サンプルAのテキストです。\n")

# sampleB.txt を作成
with open('sampleB.txt', 'w') as f:
    f.write("これはサンプルBのテキストです。\n")

# ファイルの内容をリストとして取得
with open('sampleA.txt', 'r') as f:
    sampleA_lines = f.readlines()
with open('sampleB.txt', 'r') as f:
    sampleB_lines = f.readlines()

# 差分を計算
diff = difflib.unified_diff(sampleA_lines, sampleB_lines, lineterm='', fromfile='sampleA.txt', tofile='sampleB.txt')

# 差分を表示
for line in diff:
    print(line)


# --- sampleA.txt
# +++ sampleB.txt
# @@ -1 +1 @@
# -サンプルAのテキストです。

# +これはサンプルBのテキストです。

  
### patch command: 'diff'によって生成された差分ファイル(patch file)を読み込み、指定されたファイルにその変更を適用するコマンド
# 手動ファイル編集することなく、変更を一括で反映が可能。
patch disk_usage_original.py < disk_usage.diff
# デフォルトで元のファイルを上書きしてしまうため、元のファイルをバックアップしたい場合は、-b option を使用する。
