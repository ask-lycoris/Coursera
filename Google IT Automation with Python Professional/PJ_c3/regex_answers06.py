### 未解決！L2を満たさない。

# Quiz: An intern implemented a zip code checker, but it works only with five-digit zip codes.
# Your task is to update the checker so that it includes all nine digits of the zip code; the leading five digits
# and the optional four after the hyphen. The zip code needs to be preceded by at least one space, and cannot be at
# the start of the text. Update the regular expression.

def check_zip_code (text):
 #result = re.search(r".*\s+\d{5}-\d{4}.*", text)
 result = re.search(r"^[^\s].*\s+\d{5}(-\d{4})?", text)
 return result != None

print(check_zip_code("The zip codes for New York are 10001 thru 11104.")) # True
print(check_zip_code("90210 is a TV show")) # True
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001.")) # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.")) # False
