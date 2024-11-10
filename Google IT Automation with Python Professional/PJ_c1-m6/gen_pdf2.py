#ここではデータビジュアライズのライブラリを使用して Dataframework形式 を使用してグラフ化したりした結果をpdf化しようと思う。
# 多分機能的に、pdf化 と dataの可視化でグラフを pngとして出力するのは分けた方がよさそうだけど、pdf化するのはなんかライブラリで一発な気もするので、一個のファイルでもいいかもね。

!pip install pandas seaborn matplotlib

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# DataFrameに変換
info = ["mailserver.local",":", "taylor, casey, sam, blake"]
df = pd.DataFrame(info)

# Seabornを使用して棒グラフを作成
plt.figure(figsize=(8, 6))
sns.barplot(x='カテゴリ', y='値', data=df, palette='viridis')

# グラフのタイトルとラベルを設定
plt.title('カテゴリごとの値')
plt.xlabel('カテゴリ')
plt.ylabel('値')

# PDFとして保存
plt.savefig('output.pdf', format='pdf')

# グラフを表示
plt.show()
