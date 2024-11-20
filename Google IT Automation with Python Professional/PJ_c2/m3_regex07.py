### Case with repeated the same characters ###
# 下記の方法を取ることで、単語のパーサーが非常に便利になっている
# おそらく、pythonがLLMに強い？のはこの辺に起因しているんだろう...。

import re

# search(): 文字列の中から最初に見つかったパターンを探し出す。
# 戻り値: マッチした部分の情報を持つオブジェクト（re.Match）、見つからなかった場合は None
print(re.search("[a-zA-Z]{5}", "a ghost"))
# <re.Match object; span=(2, 7), match='ghost'>

# findall(): 文字列の中からパターンに一致するすべての部分を探し出す。
# 戻り値: マッチした部分のリスト、マッチがなければ、空リスト
print(re.findall(r"[a-zA-Z]{5}", "A scary ghost appeared"))
# ['scary', 'ghost', 'appea']   ---> 単語を抽出し、5文字で抽出

# '\b':  \b は「単語境界」を意味する。
# 今回は、指定したパターンが単語として独立している場合にのみマッチさせている。
# ---> 要は、内部的には空白文字列を認識する(= 単語として独立し、隣接文字が存在しない)ようにコーディングされてるってこと。
print(re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared"))
# 'scary', 'ghost']   ---> 5文字単語だけ抽出成功

# '\w': \w は「単語」を意味する。
# 5文字以上7文字以下の文字列をマッチ
print(re.findall(r"\w{5,7}", "I really love strawberry"))
# 5文字以上10文字以下の単語をマッチ
print(re.findall(r"\b\w{5,10}\b", "I really love strawberry"))
# 5文字以上の文字列をマッチ
print(re.findall(r"\w{5,}", "I really love strawberries"))
# 20文字以下の文字列をマッチ
print(re.findall(r"\w{,20}", "I really love strawberries"))
#['really', 'strawbe']
# ['really', 'strawberry']
# ['really', 'strawberries']
# ['I', '', 'really', '', 'love', '', 'strawberries', '']

# 20文字以下の単語マッチ
print(re.findall(r"\w{,20}", "I really love strawberries."))
# ['I', '', 'really', '', 'love', '', 'strawberries', '', '']  ---> スペースも含まれてしまう。


### sample2
# Extract over 7 letters from each sentences.
def long_words(text):
  pattern = "\w{7,}"
  result = re.findall(pattern, text)
  return result

print(long_words("I like to drink coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []
