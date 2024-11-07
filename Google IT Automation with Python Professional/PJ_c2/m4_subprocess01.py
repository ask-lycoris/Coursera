# スクリプトでシステムコマンド実行可能
# プロセスも親子関係を持つことが可能
# 親プロセスは子プロセスが終了するまでexecuteをblockされ、なにも実行できない

# cp, chmod, sleepなど有力な出力が存在しないシステムコマンドを実行した際に成功したのか失敗したのかを確認したいだけのときやSTDOUT
# の内容を気にしない際に非常に有効
import subprocess

result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
# アクセス可能な完成したプロセスインスタンス(=CompletedProcess object)が返り値として得られる。
print(result.returncode)
print(result.stdout)    # b'8.8.8.8.in-addr.arpa domain name pointer dns.google.\n'
# この返り値はバイトの配列であり、「b」はこの文字列がpythonにとって適切な文字列でないことを示している。
# pythonはコマンドの出力結果をどのencodingで処理すればいいのかわかっていない場合に、バイト配列を返す。
# つまり下記のように decode すると文字列になって情報が読める。
print(result.stdout.decode().split())

result = subprocess.run(["rm", "does_not_exist"], capture_output=True)
print(result.returncode)
print(result.stdout)   # b''
print(result.stderr)   # b"rm: cannotremove 'doen_not_exist':No such file or directory\n"
# エラー'1'の際は、標準出力(stdout)は空、標準エラー出力(stderr)にエラーメッセージが格納されるようなフローになっていることが分かる。


# パス変数にディレクトリを1つ追加するプログラム
import os
import subprocess

my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])
# pathsep.joinメソッドで各OS固有のディレクトリ構成に合ったパスへ連結させてくれる

result = subprocess.run(["myapp"], env=my_env)
# パスは変更された環境下で新しいパスに書き換えられる

### Parameter of run(), if you set True...
# cws: 
# timeout: kill the process if it takes more time than expected. 停止可能性が分かっているコマンドの実行時に便利
# shell: start default system shell and you can use any commands in side it

# サブプロセスやシステムコマンドを介してpythonスクリプトで基盤となるシステムを直接インターフェースすることは、
# 特定のタスクを迅速に実行する必要がある場合に特に便利だが、意図しない変更があった場合に予期しない影響や障害が発生する場合がある。
# そのため、短時間での検証には適しているが、複雑なことや長時間実行するようなケースではpythonの組み込みモジュールや外部モジュールを使用すべし。
# サブプロセスの使用よりも標準ライブラリやpypiリポジトリをチェックして車輪の再開発を避けよう！
