# Google colab内で他の言語を使用する際は、「%%(=マジックコマンド)」を先頭につけて '%%javascript' のように指定するとその言語で動かしてくれる。
%%bash

### bashの注意点
# bashでは、変数代入時にスペースを入れてはいけない。スぺ―スもトークンとして認識されてしまう。
# よく遭遇する事例 → https://www.linux-jp.org/?p=554


### sample1: variable
echo "Starting at: $(date)"
echo

echo "UPTIME"
uptime
echo

echo "FREE"
free
echo

echo "WHO"
whoami
echo

echo "Finishing at: $(date)"

# output
# Starting at: Mon Nov 11 12:37:12 PM UTC 2024
# UPTIME
#  12:37:12 up 6 min,  0 users,  load average: 0.49, 0.55, 0.31

# FREE
#                total        used        free      shared  buff/cache   available
# Mem:        13290460      926416     7257112        1708     5106932    12036924
# Swap:              0           0           0

# WHO
# root

# Finishing at: Mon Nov 11 12:37:12 PM UTC 2024

### sample2: variable
line="-------------------------------------------------"

# $<variable>は格納した変数を適用してくれる
echo $line
echo "Starting at: $(date)"; echo $line
echo "UPTIME"; uptime; echo $line

# -------------------------------------------------
# Starting at: Mi 22. Mai 17:30:30 CEST 2019
# -------------------------------------------------
# UPTIME
#  17:30:30 up 8 days,  1:51,  2 users,  load average: 0,00, 0,00, 0,00
# -------------------------------------------------

### Globs: 正規表現みたいにコマンドラインからそのままファイルを探すことが可能。
# pytnonでこの機能を使用したいときは glob module から利用可能。
# $ echo ?????.py
# areas.py hello.py myapp.py

### Conditional Execution in Bash： 条件付き実行 (pythonにあたるif-else)
# bashでは使用される条件はコマンドの終了ステータスに基づいている。

### sample3: if-else
if grep "127.0.0.1" /etc/hosts; then
    echo "Everything ok"
else
    echo "ERROR! 127.0.0.1 is not in/etc/hosts"
fi

# output
# 127.0.0.1
# Everything ok

### Test command: true = 0, False = 1
if test -n "$PATH"; then echo "Your path is not empty"; fi   # -n: check if empty of strings
if [ -n "$PATH"]; then echo "Your path is not empty!!"; fi     # []: Alias of test command

# output
# Your path is not empty
# Your path is not empty!!

### sample4: Loop
# 特定のコマンドを実行し、そのコマンドが失敗した場合に再試行するためのループを作成している
# bashではスペースもトークンとみなされるので'='前後にスペースを入れない！
n=0
command=$1
# $commandの実行が失敗したら、&& 以降を実行する
while ! $command && [$n -lw 5]; do
  sleep $n   # 再試行のたびにnは増加するので待機時間が増加する
  ((n=n+1))
  echo "Retry #$n"
done;
