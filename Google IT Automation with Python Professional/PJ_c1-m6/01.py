# 1つのファイルにまとめて記載するとこんな感じ。

!pip install reportlab

from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

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

def provide_pdf(current_users, filename='report.pdf'):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 12)
    c.drawString(100, height - 80, "Server Name")
    c.drawString(300, height - 80, "Logged In User")

    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, height - 50, "Current logged in user Report")

    c.setFont("Helvetica", 12)
    y_position = height - 100  # 初期Y位置

    for machine, users in current_users.items():
        if users:  # ユーザーがいる場合のみ出力
            user_list = ", ".join(users)
            c.drawString(100, y_position, f"{machine}: {user_list}")
            y_position -= 20  # 次の行のY位置を下げる

            # ページの下部に達した場合、新しいページを作成
            if y_position < 50:
                c.showPage()
                c.setFont("Helvetica", 12)
                c.drawString(100, height - 80, "Server Name")
                c.drawString(300, height - 80, "Logged In User")
                y_position = height - 100  # Y位置をリセット

    c.save()


# List of events
events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
    Event('2020-01-01 08:15:23', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-02 12:45:56', 'logout', 'myworkstation.local', 'lane'),
    Event('2020-01-03 09:30:11', 'login', 'mailserver.local', 'chris'),
    Event('2020-01-04 15:53:42', 'logout', 'webserver.local', 'alex'),
    Event('2022-01-05 18:53:21', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-06 10:25:34', 'logout', 'fileserver.local', 'taylor'),
    Event('2020-01-07 11:24:35', 'login', 'dbserver.local', 'sam'),
    Event('2020-01-08 13:15:44', 'logout', 'webserver.local', 'blake'),
    Event('2020-01-09 14:30:12', 'login', 'mailserver.local', 'casey'),
    Event('2020-01-10 16:45:56', 'logout', 'myworkstation.local', 'drew'),
    Event('2020-01-11 12:50:01', 'login', 'fileserver.local', 'jordan'),
    Event('2020-01-12 09:15:23', 'logout', 'dbserver.local', 'lane'),
    Event('2022-01-13 08:45:11', 'login', 'webserver.local', 'chris'),
    Event('2022-01-14 17:53:42', 'logout', 'myworkstation.local', 'alex'),
    Event('2023-01-15 10:20:34', 'login', 'mailserver.local', 'taylor'),
    Event('2023-01-16 11:24:35', 'logout', 'fileserver.local', 'sam'),
    Event('2023-01-17 13:15:44', 'login', 'dbserver.local', 'blake'),
    Event('2024-01-18 14:30:12', 'logout', 'webserver.local', 'casey'),
    Event('2020-01-19 16:45:56', 'login', 'myworkstation.local', 'drew'),
    Event('2020-01-20 12:50:01', 'logout', 'mailserver.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'fileserver.local', 'lane'),
    Event('2020-01-22 15:53:42', 'logout', 'dbserver.local', 'chris'),
    Event('2020-01-23 18:53:21', 'login', 'webserver.local', 'alex'),
    Event('2020-01-24 10:25:34', 'logout', 'myworkstation.local', 'taylor'),
    Event('2020-01-25 11:24:35', 'login', 'mailserver.local', 'sam'),
    Event('2020-01-26 13:15:44', 'logout', 'fileserver.local', 'blake'),
    Event('2024-01-27 14:30:12', 'login', 'dbserver.local', 'casey'),
    Event('2020-01-28 16:45:56', 'logout', 'webserver.local', 'drew'),
    Event('2020-01-29 12:50:01', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-30 09:15:23', 'logout', 'mailserver.local', 'lane'),
    Event('2020-01-31 08:45:11', 'login', 'fileserver.local', 'chris'),
    Event('2030-01-01 12:00:00', 'logout', 'dbserver.local', 'alex'),
    Event('2020-01-02 14:00:00', 'login', 'webserver.local', 'taylor'),
    Event('2020-01-03 16:00:00', 'logout', 'myworkstation.local', 'sam'),
    Event('2020-01-04 18:00:00', 'login', 'mailserver.local', 'blake'),
    Event('2020-01-05 20:00:00', 'logout', 'fileserver.local', 'casey'),
    Event('2024-01-06 21:00:00', 'login', 'dbserver.local', 'drew'),
]

# Executed current data of users logged in
current_users = process_events(events)

# Generate reports
generate_report(current_users)
provide_pdf(current_users, filename='report.pdf')
