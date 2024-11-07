# スクリプトでシステムコマンド実行可能
# プロセスも親子関係を持つことが可能
# 親プロセスは子プロセスが終了するまでexecuteをblockされ、なにも実行できない

# cp, chmod, sleepなど有力な出力が存在しないシステムコマンドを実行した際に成功したのか失敗したのかを確認したいだけのときやSTDOUT
# の内容を気にしない際に非常に有効

import subprocess

result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
# アクセス可能な完成したプロセスインスタンスが返り値として得られる。
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

