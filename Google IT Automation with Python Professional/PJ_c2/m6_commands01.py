### fundamental commands related to process
# ps:現在のユーザの現在のターミナルで実行中のプロセスを一覧表示します。
# ps ax: 全てのユーザの現在実行中のプロセスを一覧表示します。  
# pse: リストされたプロセスの環境を表示します。  
# killPID: PID で識別されるプロセスに SIGTERM シグナルを送ります。
# fg: 停止中またはバックグラウンドにあるジョブをフォアグラウンドに戻します。
# bg:停止したジョブをバックグラウンドに戻します。
# jobs:現在実行中または停止中のジョブのリスト
# top:現在最も CPU 時間を使用しているプロセスを表示 (終了するには "q" を押してください) 
# free: メモリ使用量を示す。
# uptime: コンピュータの電源が入っている時間を示す。

### Management of Stream
# command >file: 標準出力をリダイレクトし、ファイルを上書きします。
# command>>file: 標準出力をリダイレクトし、ファイルに追加します。
# command <file: 標準入力をファイルからリダイレクト
# command2>file: 標準誤差をファイルにリダイレクトします。
# command1|command2: command1 の出力を command2 の入力に接続します。

# piping: Connetctheoutput of the progeam to the input ofonother in order to pass data between programs. 
#         プログラム間でデータを渡して、あるプログラムの出力を次のプログラムの入力にすることが可能。
# Linuxコマンドはスクリプトでも同様に使用でき、sysモジュールが提供するstdinファイルオブジェクトを使用して標準入力から読み込むことが可能。
# 1行ずつ書くらしい。

ls -l | less
#(... A list of files appears...)
cat spider.txt | tr ' ' '\n' | sort | uniq -c | sort -nr | head

### Signal types
# Signales are tokens delivered to running processes to indicate a desired action.
# SIGSTOP: プログラムは実際に終了せずに実行を停止する。
# 
# 'ctrl + C' : tracerouteコマンドがきれいに実行されないようにするには、 

# 'fg'   --- プログラムを再度実行させ、ctrl+C, ctrl+Z またはその他の他のシグナルでプログラムを中断するまで実行を続ける。
# 'kill' --- デフォルトではSIGTERMシグナルを送信する
# 'ps' --- プロセスを表示する。'ps aux' で実行中のすべてのプロセスを一覧表示する
