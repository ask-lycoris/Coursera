import csv

# CSVファイルのパス
csv_file = 'events.csv'

# データを格納するリスト
events = []

try:
    # CSVファイルを開く
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)  # CSVリーダーを作成
        
        # 各行をリストに追加
        for row in reader:
            events.append(row)

except FileNotFoundError:
    print(f"{csv_file} が見つかりません。")
except Exception as e:
    print(f"エラーが発生しました: {e}")

# 結果を表示
for row in events:
    print(row)
