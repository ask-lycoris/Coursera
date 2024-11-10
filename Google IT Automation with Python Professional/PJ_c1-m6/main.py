# 実際の使用を想定して、以下の修正を加えてみた。
# 1. pdfのレイアウトを修正する関数を別のファイルから呼び出して使う (gen_pdf.py)
# 2. 提供される event data は外部から excel の形として、それをimportして処理する (events.csv)
# csvの取り込みは csvライブラリ or pandasライブラリがあるが、ここでは小規模なので高速な処理の前者を採用する。
!pip install reportlab

from datetime import datetime
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

# try 内でエラー（例外）が発生すると、Python はその時点での処理を中断し、対応する except blockを探す。
try:
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        # このまま実行すると、timestampのunmatch errorが出力されてしまう。これはcsvファイルのヘッダーも読み込まれているからである。
        # 下記のように最初の行はスキップするように修正する必要がある。
        next(reader)
        # 上記readerには [' ',' ',' ',' '] とリストが格納されている
        # 各行を *Eventインスタンスに変換して* リストに追加していく
        for row in reader:
          # この後に実行するインスタンス化に伴い、左と右の変数数が一致している必要がある。
          # 一致しない時は'ValueError'が生じるため、ここでエラーハンドリングしておく。
          if len(row) != 4:  # 必要なカラム数を確認
              print(f"Row does not contain 4 columns: {row}")
              continue  # 行をスキップ
          else:
              # アンパッキング：リストやタプルなどのコレクションから要素を個別の変数に分解して割り当てる操作。  
              event_date, event_type, machine_name, user = map(str.strip, row)
              # Eventを使用してeventをインスタンス化する！この変換する工程が大事！
              # これがないと単にcsvから読み込んだ文字列データをeventsに突っ込むだけになっててAttribute Error(属性エラー)となる
              event = Event(event_date, event_type, machine_name, user)
              # eventsリストにインスタンス化したeventを追加
              events.append(event)
except FileNotFoundError:
    print(f"{csv_file} cannot be found.")

except Exception as e:
    print(f"Error processing row {row}: {e}")

# Executed current data of users logged in
current_users = process_events(events)

# Generate reports
generate_report(current_users)
provide_pdf(current_users, filename='report.pdf')
