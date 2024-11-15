import pandas as pd
import numpy as np

# Create sample data with dictionary
data = {
    'EmployeeID': range(1, 21),  # 1から20までのID
    'Name': [f'Employee {i}' for i in range(1, 21)],  # Employee 1 から Employee 20
    'Age': np.random.randint(22, 60, size=20),  # 22から60の間のランダムな年齢
    'Salary': np.random.randint(30000, 120000, size=20),  # 30000から120000の間のランダムな給与
    'HireDate': pd.date_range(start='2015-01-01', periods=20, freq='YE')  # 2015年からの年次雇用日
}

# Create DataFrame
df = pd.DataFrame(data)
# Display Dataframe
print(df)

# Extract infomation of each types from DataFrame
print(
    f"\n\n-----Type-----\n{df.dtypes}"      # propertyであって、methodではないので()不要
    f"\n\n-----Detail1-----\n{df.describe()}"
    f"\n\n-----Detail2-----\n{df.describe(include='all')}"
    f"\n\n-----12lines-----\n{df.head(12)}"
    f"\n\n-----Summary-----\n{df.info()}\n\n"   # infoメソッドは返り値を返さないのでNone
)
# infoメソッドは標準出力に出力する
df.info()

# print(f"\n\n-----Summary-----\n{summary}\n\n-----Type-----\n{types}\n\n-----Detail-----\n{detail}\n\n-----12lines-----\n{lines}")
# # もし改行したいのであれば、以下のように各行の末尾は'\'で終わらせないと続く行とみなされず、エラーになるので注意！
# print(f"\n\n-----Summary-----\n{summary}\
#          n\n-----Type-----\n{types}\
#          n\n-----Detail-----\n{detail}\
#          n\n-----12lines-----\n{lines}")


