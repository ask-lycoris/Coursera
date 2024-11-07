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
