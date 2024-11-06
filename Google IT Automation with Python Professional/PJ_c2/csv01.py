# csv means CommaSeparated Values
# CSVファイルの各行は通常1つのデータレコードを表し、各フィールドは","で区切られる
import csv
# PJ1: Creating csv file from list
host = [["Sabrina Green","802-867-5309","System Administrator"], ["Eli Jones","684-3481127","IT specialist"], 
         ["Melody Daniels","846-687-7436"," Programmer"], ["Charlie Rivera","698-746-3357","Web Developer"]]
# PJ2: Creating csv file from dictionary
users = [{"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"}, 
          {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"}, 
          {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]

# PJ1
# Writing into csv file
with open('sample.txt', 'w') as hosts_csv:
  writer = csv.writer(hosts_csv)
  writer.writerows(hosts)    # 1度に1行ずつ書き込む
  #write.write(hosts)        # 行をすべてまとめて記述する

# Reading text file and convert into csv file.
f = open("sample.txt")
# Use reader function of csv module which interpret the file as a CSV.
csv_f = csv.reader(f)

for row in csv_f:
  name, phone, role = row
  print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))
# list[0]などで指定してvalueを取ってくる方法もあるが、大量にデータがあると大変である。上記のようにリストを名前変数に展開してforで回すと、あとコードの解析がしやすくなる。


# PJ2
# Writing into csv file
keys = ["name", "username", "department"]
with open('by_department.csv', 'w') as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)
# Reading
with open('by_department.csv') as software:
  reader = csv.DictReader(software)
  for row in reader:
    print(("{} belongs to {} Department").format(row["name"], row["department"]))


# sample.txt
Sabrina Green,802-867-5309,System Administrator
Eli Jones,684-3481127,IT specialist
Melody Daniels,846-687-7436, Programmer
Charlie Rivera,698-746-3357,Web Developer

# sample data-2
name,username,department
Sol Mansi,solm,IT infrastructure
Lio Nelson,lion,User Experience Research
Charlie Grey,greyc,Development
