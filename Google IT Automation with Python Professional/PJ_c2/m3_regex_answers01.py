# Quiz1: 英数字（アルファベット、数字、アンダースコアも含む）、ピリオド、ダッシュ、プラス記号を含み、その後にピリオドと、".com"、".info"、".edu "などの文字のみのトップレベルドメインが続くかどうか

import re
def check_web_address(text):
  # pattern = "^[\w\.+-]+*\.[a-zA-Z]$"  ---> 私が最初に書いたパターン。惜しい？
  pattern = "^[\w\.-]+(\.[\w\.-]+)*\.[a-zA-Z]+$"
  # 文字列としてマッチさせたい「+」をどこに持ってくるかがキモな気がした。
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True
