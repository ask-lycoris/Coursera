# bash scripts for syslog
%% bash

### sample1



### sample2
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
