# Regex expression 正規表現
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
# 正規表現における量指定子
# '+' = 直前の要素が1回以上連続して出現することを示す
# '*' = 直前の要素が0回以上連続して出現することを示す
# '.' = 改行を除いた任意の1文字を示す

try:
  print(re.search(r"[aA]++", "banana"))     # ---> '++'という形は正規表現の文法には存在しない！
except:
  pass

print(re.search(r"[aA].*[aA]", "pineapple"))

# Escape Sequence
print(re.findall(r'\w+', "Hello, world!! 12-34_abc?$?DEF"))   # ['Hello', 'world', '12', '34_abc', 'DEF']
# \n: newline 改行
# \t: Tab
# \w: word 英数字(a-zA-Z0-9)とアンダースコア(_)
# \W: not \w
# \d: digit 数字(0-9)
# \D: not \d
# \s: space 空白文字(Space, Tab, 改行)
# \S: not \s
# ref[https://regex101.com/]   ---> 正規表現の解析サイト
# 正規表現の各部分についての詳細な説明が表示され、特定のエスケープシーケンスや構文の意味が理解できる
# 使用しているプログラミング言語に合わせた正規表現のコードスニペットを生成する

# Quiz1: 1つ以上の空白文字で区切られた少なくとも2つの英数字（文字、数字、アンダースコアを含む）グループを持っているか
# 字面だけ追ってると、条件が良くわからんな。どういうケースをマッチ対象としたいのか先に具体例をいくつか示された方が書けそう...。
def check_character_groups(text):
  result = re.search(r"\w+\s+\w+", text)
  return result != None

# samples
print(check_character_groups("One")) # False
print(check_character_groups("123    Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False

# Quiz2: 標準的な文かどうか
def check_sentence(text):
  result = re.search(r"^[A-Z].*[.!?]$", text)
  return result != None

# 下記両者は異なる概念！だが、両方で使用される記号 「?」「*」「.」があるからややこしい
### Wildcard ###
# 主にファイルやフォルダ操作に使用。コマンドラインやファイル検索で使用する = だから「.」だけ該当外になってるのだと思う
# ex. *.txt      ---> <任意の0文字以上の文字列> + .txt     = すべての.txt拡張子がマッチ
#     ワイルドカードでの文脈で「.」は存在しないと考えてよい！
#     file?.txt  ---> file + <任意の1文字> + .txt         = 'fileA.txt' などがマッチ
  
### Regex ###
# プログラミングやテキスト処理で使用。文字列パターン検索で使用する。
# ex. ab*c       ---> 直前の文字が0以上出現する             = 'ac','abc','abbbc'などがマッチ
#     a.b        ---> a + <任意の1文字> + b                = 'acb','a1b','a!b'などがマッチ、'ab'や'a\nb'はマッチしない 
#     colou?r    ---> 直前の文字が 0回 or 1回 のみ出現する   = 'color','colour'などがマッチ、'colouur'はマッチしない
