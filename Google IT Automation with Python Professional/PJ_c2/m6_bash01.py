# Google colab内で他の言語を使用する際は、「%%(=マジックコマンド)」を先頭につけて '%%javascript' のように指定するとその言語で動かしてくれる。
%%bash

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
