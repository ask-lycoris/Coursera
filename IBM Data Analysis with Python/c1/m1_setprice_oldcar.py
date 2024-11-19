# Run bash script below to create sample csvfile before run this script.
# %%bash
# curl -O https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_base.csv
# -O option can save the file witn original name.

!pip install numpy pandas

import requests
import pandas as pd
import numpy as np

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
df.head(20)


print(df.describe(include='all'))
print(df.info())
