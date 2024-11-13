# bash scripts for syslog
%% bash
### sample1: Loop
for logfile in /var/log/*log; do
    echo "Processing: $logfile"
    cut -d' ' -f5- $logfile | sort | uniq -c | sort -nr | head -5
done


### sample2: cut
# contents
# Oct 10 12:34:56 hostname some message here
echo "Oct 10 12:34:56 hostname some message here" > /var/log/syslog_sample
tail /var/log/syslog_sample | cut -d' ' -f3    # '-'：cutコマンドにおいてx番目のフィールドの前後を指すトークン
tail /var/log/syslog_sample | cut -d' ' -f3-
tail /var/log/syslog_sample | cut -d' ' f3-    # こういう書き方はないようだ...

# output
12:34:56
12:34:56 hostname some message here
CalledProcessError

# sample3: human readable
# コードが複雑すぎる場合や、platform間で互換性が必要な場合は、pythonか標準ライブラリを使用するように。
import sys

for i in sys.stdin:
  words = line.strip().split()
  print("".join([word.capitalize() for word in words]))
