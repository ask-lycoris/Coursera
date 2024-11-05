# 書き込む内容
class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = datetime.strptime(event_date, '%Y-%m-%d %H:%M:%S')  # 日付をdatetimeオブジェクトに変換
        self.type = event_type
        self.machine = machine_name
        self.user = user

content = """ events = [
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
]"""

# ファイルに上書きで書き込む
with open('events.csv', 'w') as file:
    file.write(content)

print("ファイルに書き込みました。")

# 中身確認
with open(csv_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
