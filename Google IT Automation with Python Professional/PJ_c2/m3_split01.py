# split()と同様に機能するが、デリミタに区切り文字ではなく、正規表現を指定することが可能
import re

print(re.split(r"[.?!]", "One sentence. Another one? And the last one!"))
print(re.split(r"([.?!])", "One sentence. Another one? And the last one!"))   # ()がつくか否か
print(re.split(r"the|a", "One sentence. Another one? And the last one!"))

# ['One sentence', ' Another one', ' And the last one', '']
# ['One sentence', '.', ' Another one', '?', ' And the last one', '!', '']
# ['One sentence. Ano', 'r one? And ', ' l', 'st one!']


# sub() : 分割と置換の両方に正規表現を適用する
print(re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@my.example.com"))

# Received an email for [REDACTED]

# replaceにキャプチャグループを適用する(詳細はm4で)
print(re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada"))
                 -------     -------        -- --
                   第1G        第2G    \2=2番目のキャプチャグループに相当   \1=1番目のキャプチャグループに相当   ---> つまり入れ替わるだけ！
# 第一引数：検索するパターン（正規表現）を指定。
# 第二引数：置き換え後の文字列を指定。
# 第三引数：置き換えを行う元の文字列を指定。

# Ada Lovelace








