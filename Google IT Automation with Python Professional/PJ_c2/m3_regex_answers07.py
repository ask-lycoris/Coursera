import re

### sample1
# You’re working with a CSV file that contains employee information. Each record has a name field, followed by a phone number field, and a role field.
# The phone number field contains U.S. phone numbers and needs to be modified to the international format, with +1- in front of the phone number.
# The rest of the phone number should not change. Fill in the regular expression, using groups, to use the transform_record() function to do that.
def transform_record(record):
  new_record = re.sub(r"(\d{3}-\d{3}-\d{4})", r"+1-\1", record)
                                               #   ---   \1=キャプチャグループで第1Gを指すので、置換前のものに「+1-」を付け足すようになっている。
  return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator"))
print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# Sabrina Green,+1-802-867-5309,System Administrator
# Eli Jones,+1-684-3481127,IT specialist


### sample2
# Question 2
# The multi_vowel_words() function returns all words with 3 or more consecutive vowels (a, e, i, o, u). Fill in the regular expression to do that.
def multi_vowel_words(text):
  pattern = r'\b\w*[aeiou]{3,}\w*\b'
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful")) 
# ['beautiful']
print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) 
# ['Obviously', 'queen', 'courageous', 'gracious']
print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) 
# ['rambunctious', 'quietly', 'delicious']
print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)")) 
# ['queue']
print(multi_vowel_words("Hello world!")) 
# []


### sample3
# Question 4
# The transform_comments() function converts comments in a Python script into those usable by a C compiler. This means looking for text that begins with a hash mark (#) and replacing it with double slashes (//),
# which is the C single-line comment indicator. For the purpose of this exercise, we'll ignore the possibility of a hash mark embedded inside of a Python command, and assume that it's only used to indicate a comment.
# We also want to treat repetitive hash marks (##), (###), etc., as a single comment indicator, to be replaced with just (//) and not (#//) or (//#). Fill in the parameters of the substitution method to complete this function: 
def transform_comments(line_of_code):
  result = re.sub('#+','//',line_of_code)
  return result

print(transform_comments("### Start of program")) 
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable")) 
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable")) 
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)")) 
# Should be "  return(number)"


### sample4
# The convert_phone_number() function checks for a U.S. phone number format: XXX-XXX-XXXX (3 digits followed by a dash, 3 more digits followed by a dash, and 4 digits),
# and converts it to a more formal format that looks like this: (XXX) XXX-XXXX. Fill in the regular expression to complete this function.
def convert_phone_number(phone):
    # 正規表現で電話番号の形式をキャプチャし、置換する
    result1 = re.sub(r"(\d{3})-(\d{3})-(\d{4})", r"(\1) \2-\3", phone)     # これだと、L3が (123)-123-12345 となってしまい、回答に合致しないので、第3Gの数字が4桁目で終わり(5桁目以上続かない)にマッチさせる必要がある
    result2 = re.sub(r"(\d{3})-(\d{3})-(\d{4})\b", r"(\1) \2-\3", phone)   # \b を付与することによって区切り文字スペースを競ってすることができ、単語で区切る古語が可能となる。
    return result1, result2

print(convert_phone_number("My number is 212-345-9999."))  # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234"))    # Please call (888) 555-1234
print(convert_phone_number("123-123-12345"))               # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300"))  # Phone number of Buckingham Palace is +44 303 123 7300
