# データが大量にあるときはすべてを読み込んでから解析するのではなく、1行1行読み下しながら処理していく方法がbetter
# Quiz: ここでは、サーバの挙動がおかしいのをログファイルから精査していくシナリオに取り組む。
# どうやら誰かがcron jobを起動した影響らしいことが分かった。ログを精査して誰がどの頻度でcronjobを開始したのかを正確に特定したい。

# このスクリプトは実行時に引数を1つ持ち、解析したいログファイルであることが期待される。
#!/user/bin/env python3
import re
import sys

# sys moduleはpythonインタプリタに関する情報や操作を提供する
# sys.argvはコマンドライン引数を格納するリストであり、コマンドラインから渡された最初の引数をlogfile変数に格納している。
logfile = sys.argv[1]
# なお、「$ ./script.py xxx」 としたとき、
# sys.argv[0] = ./script.py   ---> スクリプトのパス
# sys.argv[1] = xxx となる。   ---> 第1引数

# ログインユーザ名を値をforで回して回数増やしていく代わりに、ユーザ名とその出現回数を格納するための空の辞書を作成する。
usernames = {}
with open(logfile) as f:
  for line in f:
    # CRON が含まれない場合は無視
    if "CRON" not in line:
      continue   # ---> passと何が違うのか？
    # capture group
    pattern = r"USER \((\w+)\)$"
    result = re.search(pattern, line)
    # パターンマッチしなかった場合は無視
    if result is None:
      continue
    name = result[1]
    # nameには正規表現によってマッチしたキャプチャグループの1番目、つまり"ユーザ名"が格納されている
    usernames[name] = usernames.get(name, 0) + l
print(usernames)

### continueとpassの違い
# 両社は制御フローに関するもの。
# 表面上の挙動は同じように見える場合があるが、ループ内でそれ以後の処理をスキップするか否かが大きく違う点である。
# continue = 現在のループの残りは全てスキップされ、次のループ反復が始まる。特定条件下でのループ処理のフローの変更が目的。
# pass = 何もしないことを明示的に示すために使用される。将来実装を追加する可能性を示唆する。可読性の向上が目的。
# for i in range(5):
#     if i % 2 == 0:
#         continue
#         print("Even number")   ---> 偶数の場合はprint行はスキップされるため出力されない
#     print("Odd number:", i)

# for i in range(5):
#     if i % 2 == 0:
#         pass  # 特に何もしないが、ここに何かを書く予定があるかもしれない
#         print("Odd number")    ---> 偶数の場合でもpassが何もしない行なだけで、print行は機能し出力される
#     print("Current number:", i)
