### sample1
# You have a list of website urls that includes both securely encrypted websites that begin with https://www. and the unencrypted websites that begin with http://. The list includes websites that end in .com and .co. 
# Complete the secure_website_domain() function so it returns the part of the website between www. and the last part of the url (.com or .co) for only the secure websites. 
import re

def secure_website_domain(website):
    # Regex pattern to match 'https://' followed by the domain name
    pattern = r"https://([\w.-]+)"  # Capturing the domain after 'https://'
    result = re.findall(pattern, website)  # Use re.findall to get matches
    if not result:  # If result is empty (no matches found)
        return ""
    return result[0]  # Return the first capturing group

print(secure_website_domain("http://www.text.com"))  # Should return nothing
print(secure_website_domain("https://www.text.com"))  # Should return 'www.text.com'
print(secure_website_domain("http://www.text.co"))  # Should return nothing
print(secure_website_domain("https://www.text.co"))  # Should return 'www.text.co'


### sample2
# You are exploring the punctuation at the end of sentences and want to split sentences so that each word is separate and any punctuation is included in the word next to it.
# Complete the parse_sentences() function to accomplish this task.
def parse_sentences(sentence):
 pattern = r"\w+[\w'.,!?]*"  # 単語とその後の句読点を含む
 result = re.findall(pattern, sentence) #enter the re method  here
 return result

print(parse_sentences("Hello! How are you doing?")) # should return ['Hello!', 'How', 'are', 'you', 'doing?']
print(parse_sentences("what a beautiful day it is")) # should return ['what', 'a', 'beautiful', 'day', 'it', 'is']
print(parse_sentences("2 + 2 is definitely 4!")) # should return ['2', '+', '2', 'is', 'definitely', '4!']


### sample3
# International Standard Book Numbers (ISBNs) are used to uniquely identify published books. They follow a 13-digit format: 
# XXX-X-XX-XXXXXX-X
# where each X represents one numeric digit. You have a list of books, information about those books, and their ISBN numbers. You want to extract the 6 digits of the ISBN that come before the last hyphen of each book’s ISBN number.
# However, you need to be careful to avoid 6-digit strings that are not part of the ISBN numbers you’re interested in. 
# Complete the find_isbn() function so you can use it to extract the 6-digit portion of the ISBN numbers of the books on your list. 
def find_isbn(s):
    pattern = r"(\d{3})-(\d{1})-(\d{2})-(\d{6})-(\d{1})"  # ISBNの正規表現パターン
    match = re.match(pattern, s)  # 文字列の先頭からパターンにマッチするか確認
    if match:
        return match.group(4)  # 4番目のキャプチャグループを返す
    return ""  # マッチしなかった場合は空文字列を返す

print(find_isbn("123-4-12-098754-0")) # Should return 098754
print(find_isbn("223094-AB-30")) # result should be blank
print(find_isbn("1123-4-12-098754-0")) # result should be blank

# 仮に以下のように書いたとすると...
# 're.sub()' は、指定した正規表現パターンに一致する部分を新しい文字列で置き換えるためのメソッド。
# マッチした場合：置換後の文字列を格納
# マッチしなかった場合：置換前の文字列を格納。
# したがって、マッチしなかった場合に result が None になることはなく、if文に入って "" を返すことはない！！
# def find_isbn(list):
#   pattern = r"(\d{3})-(\d{1})-(\d{2})-(\d{6})-(\d{1})" #enter the regex pattern here
#   result = re.sub(pattern, r"\4", list) #enter the re method  here
#   if result is None:
#     return ""
#   return result #return the correct capturing group


### sample4
def find_url(website):
 #pattern = "https://\w+.*[^/\s]*"             # これだと、なんかセンテンスまで出力されてしまう
 pattern = "https://[a-zA-Z0-9.-]+[^/\s]*"
 result = re.findall(pattern, website)         # enter the re method here
 return result
  
print(find_url("Go to the website https://www.coursera.com find more information about Google Certificate Programs. Then, visit https://www.python.org/ to learn more about Python. ")) # Should return ['https://www.coursera.com', 'https://www.python.org']
print(find_url("You can find anything on https://www.google.com!")) # Should return ['https://www.google.com']
print(find_url("You can find anything on http://www.google.com!")) # Should return []
print(find_url("Check out python.org!")) # Should return []


