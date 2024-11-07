import re

def check_punctuation (text):
  ### 英数字以外ならヒット
  result = re.search(r"[^a-zA-Z0-9]", text)
  ### 句読点が含まれるならヒット
  result2 = re.search(r"[,\.;!?]", text) # ---> ポイントは、ドットワイルドカードを\(エスケープ)する点。
  return result2 != None

# samples
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
# "+" = 正規表現において1回以上の繰り返しを表す量指定子、直前の要素が1回以上連続して出現することを示す

try:
  print(re.search(r"[aA]++", "banana"))     # ---> '++'という形は正規表現の文法には存在しない！
except:
  pass

print(re.search(r"[aA].*[aA]", "pineapple"))

# escape sequence
print(re.findall(r'\w+', "Hello, world!! 12-34_abc?$?DEF"))   # ['Hello', 'world', '12', '34_abc', 'DEF']
# \n: newline 改行
# \t: Tab
# \w: word 英数字(a-zA-Z0-9)とアンダースコア(_)
# \W: not \w
# \d: digit 数字(0-9)
# \D: not \d
# \s: space 空白文字(Space, Tab, 改行)
# \S: not \s

# Quiz: 1つ以上の空白文字で区切られた少なくとも2つの英数字（文字、数字、アンダースコアを含む）グループを持っているか
# 字面だけ追ってると、条件が良くわからんな。どういうケースをマッチ対象としたいのか先に具体例をいくつか示された方が書けそう...。
def check_character_groups(text):
  result = re.search(r"\w+\s+\w+", text)
  return result != None

# samples
print(check_character_groups("One")) # False
print(check_character_groups("123    Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False
