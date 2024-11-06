### For this lab, imagine you are an IT Specialist at a medium-sized company.
### The Human Resources Department at your company wants you to find out how many people are in each department.
### You need to write a Python script that reads a CSV file containing a list of the employees in the organization,
### counts how many people are in each department, and then generates a report using this information.
### The output of this script will be a plain text file.

#下記のコメントは違うところに移植してね、あとで。
# 仮想マシン（VM）とは、ソフトウェアでシミュレートされたコンピュータのことだ。必要なハードウェアからマシン内部で稼働しているオペレーティングシステムまでをシミュレートする。
# Qwik lab

#!/usr/bin/env python3

import csv

def read_employees(csv_file_location):
  # register_dialectメソッド from csvモジュール
  # 異なるCSV形式に対し、特定のフォーマット(Dialect)を簡単に定義することで可読性や保守性を向上させ、再利用することを可能にする。
  # CSVファイルは","や";"など区切り文字がバラバラ。この場合、delimiterパラメータなどを使用することで各ファイル形式に合わせた設定を登録することが可能。
  csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
  # 第1引数=ダイアレクト名登録, 第2引数=カンマ後の空白無視, 第3引数=CSVファイルが正しい形式であることを確認 ---> 予期しないデータの読み込みを防ぐ
  csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
  # csv.DictReader() = 指定されたCSVファイルを読み込み、各行を辞書形式で保管する
  employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
  employee_list = []
  for data in employee_file:
    employee_list.append(dict(data))

  return employee_list

employee_list = read_employees('/home/student/data/employees.csv')

def process_data(employee_list):
  department_list = []
  for employee_data in employee_list:
    department_list.append(employee_data['Department'])
  department_data = {}
  for department_name in set(department_list):
    department_data[department_name] = department_list.count(department_name)

  return department_data

dictionary = process_data(employee_list)

def write_report(dictionary, report_file):
  with open(report_file, "w+") as f:
    for k in sorted(dictionary):
      f.write(str(k) + ':' + str(dictionary[k]) + '\n')
    f.close()

write_report(dictionary, '/home/student/test_report.txt')
