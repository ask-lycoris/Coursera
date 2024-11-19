# Run bash script below to create sample csvfile before run this script.
# %%bash
# curl -O https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_base.csv
# -O option can save the file witn original name.

!pip install numpy pandas

import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def download(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Downloaded {filename}")
    else:
        print(f"Failed to download {url}: {response.status_code}")

# We cannot use dynamic function on Google colab.
# async def download(url, filename):
#     response = await pyfetch(url)
#     if response.status == 200:
#         with open(filename, "wb") as f:
#             f.write(await response.bytes())

file_name='laptop_pricing_dataset_base.csv'

# Create DataFrame by reading csv file
df = pd.read_csv(file_name, header=None)

print("The first 5 rows of the dataframe") 
df.head(5)

### output here ###
# The first 5 rows of the dataframe
# Acer	4	IPS Panel	2	1	5	35.56	1.6	8	256	1.6.1	978
# 0	Dell	3	Full HD	1	1	3	39.624	2.0	4	256	2.2	634
# 1	Dell	3	Full HD	1	1	7	39.624	2.7	8	256	2.2	946
# 2	Dell	4	IPS Panel	2	1	5	33.782	1.6	8	128	1.22	1244
# 3	HP	4	Full HD	2	1	7	39.624	1.8	8	256	1.91	837
# 4	Dell	3	Full HD	1	1	5	39.624	1.6	8	256	2.2	1016

# create headers list
# headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
#          "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
#          "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
#          "peak-rpm","city-mpg","highway-mpg","price"]
headers = ["Manufacturer", "Category", "Screen", "GPU", "OS", "CPU_core", "Screen_Size_inch", "CPU_frequency", "RAM_GB", "Storage_GB_SSD", "Weight_kg", "Price"]
print("The number of headers", len(headers))

# headerの追加
current_headers = df.columns.tolist()

# 元のカラム数が不足している場合、新しいカラムを追加
if len(current_headers) < len(headers):
    for header in headers[len(current_headers):]:
        df[header] = np.nan  # 新しいカラムにNaNを設定

# カラム名を更新
df.columns = headers

# DataFrame内のすべての'?'をNaNに置き換え。データの欠損値を適切に扱うための前処理。
df1=df.replace('?',np.NaN)

# "Price"カラムにNaNが含まれる行を削除。価格情報欠損値の前処理。
df=df1.dropna(subset=['Price'], axis=0)
print(df.head(20))

# データセットの要約統計量を表示し、データの分布や特徴を確認
# df.describe(include='all')
# DataFrame の構造に関する情報を表示し、データの状態を把握
# df.info()

# スペックスコアを計算
columns_to_score = ['GPU', 'CPU_core', 'CPU_frequency', 'RAM_GB', 'Storage_GB_SSD']
min_values = df[columns_to_score].min()
max_values = df[columns_to_score].max()

def calculate_score(column, min_val, max_val):
    return ((column - min_val) / (max_val - min_val)) * 10

for column in columns_to_score:
    df[f'{column}_Score'] = calculate_score(df[column], min_values[column], max_values[column])

df['Spec_Score'] = df[[f'{column}_Score' for column in columns_to_score]].sum(axis=1)
df['Cost_Performance'] = df['Spec_Score'] / df['Price']

# 最もスペックの良いPCとコストパフォーマンスの良いPCを特定
best_specs_index = df['Spec_Score'].idxmax()
best_cost_performance_index = df['Cost_Performance'].idxmax()

# 各メーカーに異なる色を割り当て
unique_manufacturers = df['Manufacturer'].unique()
colors = sns.color_palette("Paired", len(unique_manufacturers))
color_map = {manufacturer: colors[i] for i, manufacturer in enumerate(unique_manufacturers)}

# バブルチャートのデータを準備
sizes = df['Price'] * 1  # バブルのサイズを価格に基づく
scatter_colors = [color_map[manufacturer] for manufacturer in df['Manufacturer']]
scatter_alpha = 0.7
# エッジカラーの設定
edge_color = ['blue' if i == best_specs_index or i == best_cost_performance_index else 'white' for i in range(len(df))]

# バブルチャートを一括で描画
plt.scatter(
    df['Cost_Performance'],
    df['Spec_Score'],
    s=sizes,
    alpha=scatter_alpha,
    color=scatter_colors,
    edgecolors=edge_color
    )

# チャートの詳細設定
plt.title('Cost Performance and Spec Performance in Each PC Manufacturer')
plt.xlabel('Cost Performance')
plt.ylabel('Spec Performance')
plt.grid(True)
plt.xlim(left=0, right=df['Cost_Performance'].max() * 1.1)
plt.ylim(bottom=0, top=df['Spec_Score'].max() * 2)

# メーカー名称とカラーを紐づけた表を作成
fig, ax = plt.subplots(figsize=(3, 1))
color_df = pd.DataFrame(list(color_map.items()), columns=['Manufacturer', 'Color'])

table_data = []
for i, row in color_df.iterrows():
    table_data.append([row['Manufacturer'], ''])  # 空欄を追加
table = ax.table(cellText=table_data, colLabels=['Manufacturer', 'Color'], cellLoc='center', loc='center')

for i, (manufacturer, color) in enumerate(zip(color_df['Manufacturer'], color_df['Color'])):
    table[(i + 1, 1)].set_facecolor(color)

table.auto_set_font_size(True)
ax.axis('off')
table.scale(1, 1)

# 最もスペックの良いPCとコストパフォーマンスの良いPCを整理
best_specs_company = df['Manufacturer'].iloc[best_specs_index]
best_specs_value = df['Spec_Score'].iloc[best_specs_index]
best_cost_performance_company = df['Manufacturer'].iloc[best_cost_performance_index]
best_cost_performance_value = df['Cost_Performance'].iloc[best_cost_performance_index]

# 結果の表示
plt.show()
print(f'Most Powerful PC Manufacturer: {best_specs_company} with Spec Score: {best_specs_value}')
print(f'Best Cost Performance Manufacturer: {best_cost_performance_company} with Cost Performance: {best_cost_performance_value}')
