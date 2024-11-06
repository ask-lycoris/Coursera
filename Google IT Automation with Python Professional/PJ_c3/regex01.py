import re

def check_punctuation (text):
  ### 英数字以外ならヒット
  result = re.search(r"[^a-zA-Z0-9]", text)
  ### 句読点が含まれるならヒット
  result2 = re.search(r"[,\.;!?]", text) # ---> ポイントは、ドットワイルドカードを\(エスケープ)する点。
  return result2 != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False

# reモジュールのsearchメソッドではどんな形で返ってくるのか？
print(re.search(r"o+l+", "boil"))              # <_sre.SRE_Match object; span=(1, 3), match='ol'>
print(re.search(r"o+l+", "woolly"))            # <_sre.SRE_Match object; span=(1, 5), match='ooll'>
print(re.search(r"p?each", "I like peaches"))  # <_sre.SRE_Match object; span=(7, 12), match='peach'>
# 出力結果を見ると、最初に見つかったマッチオブジェクトを返していることが分かる。
# マッチ開始位置と終了位置インデックス情報とマッチ文字情報
# マッチが見つからなかった場合は None を返す。


