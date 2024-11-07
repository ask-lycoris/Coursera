### 未解決！！

# Quiz: テキストに括弧で囲まれた2文字以上の文字または数字があるかどうかをチェックし、少なくとも最初の文字が大文字（文字の場合）であることを確認します。条件を満たす場合はTrue を返し、そうでない場合はFalse を返す。
# 例えば、"Instant messaging (IM) is a set of communication technologies used for text-based communication" は、(IM)がマッチ条件を満たすので、True を返す
# んーなんかL4でTrueにならないな...。

import re

def contains_acronym(text):
  #pattern = ".*\(^[A-Z]\w+).*" 
  #pattern = "\([A-Z][a-zA-Z0-9]{1,}\).*"
  pattern = ".*\([A-Z][a-zA-Z0-9]*\).*"
  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True
