!pip install numpy pandas

import requests
import pandas as pd
import numpy as np

# from pyodide.http import pyfetch

def download(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Downloaded {filename}")
    else:
        print(f"Failed to download {url}: {response.status_code}")

# async def download(url, filename):
#     response = await pyfetch(url)
#     if response.status == 200:
#         with open(filename, "wb") as f:
#             f.write(await response.bytes())

file_path='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv'

# この行でエラー出るよ
await download(file_path, "auto.csv")
file_name="auto.csv"

# Create DataFrame by reading csv file
df = pd.read_csv(file_name)

print("The first 5 rows of the dataframe") 
df.head(5)

# create headers list
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
# print("headers\n", headers)

df.columns = headers
df.columns

df1=df.replace('?',np.NaN)

df=df1.dropna(subset=["price"], axis=0)
df.head(20)
