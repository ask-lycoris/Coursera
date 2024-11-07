# スクリプトにコマンドライン引数で特定の値を受け取らせるのはIaCでも非常に役立つ！
# これによりスクリプトの汎用化ができ、インタラクティブなユーザ入力を必要とせずに自動的に実行することが可能である。
# システム管理に必須なスキル

#!/usr/bin/env python3
import sys
print(sys.argv)

# $ ./parameters.py one two three 
# ---> パラメータ3つ渡すと、['./parameters.py','one','two','three']のようにリスト型に格納されて出力される！
# The list of arguments are stored in the sys module.
# このプログラムにパラメータ(引数)を渡してスクリプトを回すと、そのデータがsys moduleの中に格納されて一緒に出力される。


#!/usr/bin/env python3
import os
import sys

filename = sys.argv[1]

if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("New file created\n")
else:
    print("Error, the file {} already exists!".format(filename))
    sys.exit(1)
