import re

print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))
# 上記でやっていることを説明する！
re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared")
# print文の中に突っ込んでなくてもstdoutに出力されるじゃん！
print(re.findall(r"\w{5,10}", "I really like strawberries"))
print(re.findall(r"\w{5,}", "I really like strawberries"))
print(re.search(r"s\w{,20}", "I really like strawberries"))
