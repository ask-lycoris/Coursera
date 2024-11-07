# 下の方に未解決空欄問題あり！！

# データが大量にあるときはすべてを読み込んでから解析するのではなく、1行1行読み下しながら処理していく方法がbetter
# ここでは、サーバの挙動がおかしいのをログファイルから精査していくシナリオに取り組む。
# どうやら誰かがcron jobを起動した影響らしいことが分かったので、ログを精査して正確に特定したい。

# このスクリプトは実行時に引数を1つ持ち、解析したいログファイルであることが期待される。
#!/user/bin/env python3
import re
import sys

logfile = sys.argv[1]
with open(logfile) as f:
  for line in f:
    if "CRON" not in line:
      continue   # ---> passと何が違うのか？
    pattern = r"USER \((\w+)\)$"
    result = re.search(pattern, line)
    print(result[1])

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
