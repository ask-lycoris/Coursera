# Quiz: 12時間時計の時刻形式を次のようにチェックする： 時は1から12の間で、先頭にゼロはなく、その後にコロンが続き、
#       分は00から59の間で、任意でスペースが続き、AMまたはPMが大文字または小文字で続く。その正規表現を記入せよ

import re
def check_time(text):
  #pattern = "(^(1[0-2]|[1-9]):([0-5][0-9])$\s*(am|AM|pm|PM)"
  # 正規表現における( ) の扱い
  # グループ化することで文字列として選択肢を付与できるのでパイプ「|」と一緒に使うことが多いかも。
  # 今回は^の外になぜか()があったせいでうまく動作しなかった。
  pattern = "^(1[0-2]|[1-9]):([0-5][0-9])\s*(am|AM|pm|PM)$"
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False
print(check_time("6:02 am")) # True
print(check_time("6:02km")) # False
