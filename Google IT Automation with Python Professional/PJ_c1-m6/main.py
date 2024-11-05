# 実際の使用を想定して、以下の修正を加えてみた。
# 1. pdfのレイアウトを修正する関数を別のファイルから呼び出して使う (gen_pdf.py)
# 2. 提供される event data は外部から excel の形として、それをimportして処理する (events.csv)
# csvの取り込みは csvライブラリ or pandasライブラリがあるが、ここでは小規模なので高速な処理の前者を採用する。
# んーなんかエラーになるなぁ。。。

!pip install reportlab

from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import csv
# 異なるファイルからユーザ関数を呼び出し
from gen_pdf import provide_pdf

csv_file = 'events.csv'

class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = datetime.strptime(event_date, '%Y-%m-%d %H:%M:%S')  # 日付をdatetimeオブジェクトに変換
        self.type = event_type
        self.machine = machine_name
        self.user = user

def get_event_date(event):  ## これがある理由が分からない
    return event.date

def process_events(events):
    # イベントを時系列に並べ替え
    events.sort(key=get_event_date)
    # events.sort(key=event.date)じゃだめなのか？
    # → event.date は Event クラスのインスタンスの属性で、events リスト内の各要素が Event インスタンスであるため、
    # 直接 event.date を使うことはできない。
    
    current_users = {}  # 現在ログインしているユーザーを保持する辞書

    for event in events:
        if event.type == "login":
            if event.machine not in current_users:
                current_users[event.machine] = set()  # マシンごとにユーザーのセットを初期化
            current_users[event.machine].add(event.user)  # ユーザーを追加
        elif event.type == "logout":
            if event.machine in current_users and event.user in current_users[event.machine]:
                current_users[event.machine].remove(event.user)  # ユーザーを削除

    return current_users

def generate_report(current_users):
    for machine, users in current_users.items():
        if users:  # ユーザーがいる場合のみ出力
            user_list = ", ".join(users)
            print (f"{machine}: {user_list}")

events = []

try:
    with open(csv_file_path, 'r', encoding='utf-8')as file:
        for row in csv.DictReader(file):
            events.append(row)
except FileNotFoundError:
    print(f"{csv_file_path} cannot be found.")
except Exception as e:
    print(f"Error: {e}")

# Executed current data of users logged in
current_users = process_events(events)

# Generate reports
generate_report(current_users)
provide_pdf(current_users, filename='report.pdf')
