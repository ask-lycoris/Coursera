# 未解決ここから
# Quiz:空欄補充
def show_time_of_pid(line):
  pattern = ____     ---> これ分からないな...。
  result = re.search(pattern, line)
  return f"{result.group(1)} pid:{result.group(2)}" 
  
print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440
print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187
print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187
print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440
print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807
print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:04:01 pid:29440
print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:05:01 pid:29440

### キャプチャグループ capture group
# 特定部分を( )で囲むことでその部分を後で取り出せるように返り値のオブジェクトの中に保管される。
# このオブジェクトからデータを取り出す際は、re moduleのsearch()やmatch()を使用して取得する。
import re

line = "Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)"
pattern = r"USER \((\w+)\)$"
result = re.search(pattern, line)
# re.searchでマッチが成功した場合、resultはMatch object (型が<class 're.Match'>) となり、マッチした情報が格納される。
print(result[0])         # USER (good_user) = 全体マッチ
print(result[1])         # good_user        = 1番目のキャプチャグループ
# マッチオブジェクトから拾ってくるときはインデックスアクセスできるみたい
print(result.group(0))   # マッチした全体の文字列を返し、引数指定で特定のキャプチャグループの文字列を取得可能。
# groupメソッドを使用する際は引数指定で取得可能。結果はインデックス指定した時と同じ挙動を示す。


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



