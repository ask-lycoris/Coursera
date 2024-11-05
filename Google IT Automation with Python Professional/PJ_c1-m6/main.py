# have to change!!　まだ途中
# 実際の使用を想定して、以下の修正を加えてみる。
# 1. pdfのレイアウトを修正する関数を別のファイルから呼び出して使う (pdf_style.py)
# 2. 提供される event data は外部から excel の形として、それをimportして処理する (sample_data.csv)

from event_data import event_data
from pdf_report import create_pdf_report

def aggregate_users(event_data):
    current_users = {}
    for event in event_data:
        if event.action == 'login':
            if event.machine not in current_users:
                current_users[event.machine] = set()
            current_users[event.machine].add(event.user)
        elif event.action == 'logout' and event.machine in current_users:
            current_users[event.machine].discard(event.user)
    
    return current_users

if __name__ == "__main__":
