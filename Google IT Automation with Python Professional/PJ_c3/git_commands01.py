＜各エリアでカテゴライズしたコマンド群＞

1. Working Directoryで使用するコマンド
Working Directory（作業ディレクトリ）は、ユーザーが実際にファイルの編集や作成を行う場所です。これに関連するコマンドは、変更を確認したり管理するために使用されます。

主なコマンド:
git status

Working Directoryの変更状況を確認。
git diff

Working Directoryでの変更を比較。
git add

Working Directoryの変更をStaging Areaに追加。
git restore

Working Directoryの変更を取り消す。
git rm

Working DirectoryとStaging Areaからファイルを削除。
git mv

Working Directoryのファイルを移動または名前変更し、それをStaging Areaに反映。
2. Staging Areaで使用するコマンド
Staging Area（インデックス）は、コミットする準備が整った変更が一時的に保存される場所です。このエリアを管理するためのコマンドは以下の通りです。

主なコマンド:
git add

Working Directoryの変更をStaging Areaに追加。
git status

Staging Areaの変更状況を確認。
git diff --cached

Staging Areaの変更を確認。
git reset

Staging Areaから変更を取り消し、Working Directoryに戻す。
git rm --cached

Staging Areaからファイルを削除（Working Directoryには影響しない）。
git commit

Staging Areaの変更をGit Directoryに保存（コミット）する。
3. Git Directoryで使用するコマンド
Git Directory（リポジトリ）は、バージョン管理のためのすべてのデータが保存されている場所です。このエリアに関連するコマンドは、履歴管理やリポジトリ操作に関するものが中心です。

主なコマンド:
git commit

Staging Areaの変更をGit Directoryに記録。
git log

コミット履歴を表示。
git reflog

HEADの移動履歴を表示。
git branch

ブランチを管理。
git checkout / git switch

指定したブランチやコミットに移動。
git reset

Git DirectoryのHEADやStaging Areaの状態を以前の状態に戻す。
git stash

Working DirectoryやStaging Areaの変更を一時保存し、Git Directoryに影響を与えない。
git fetch

リモートリポジトリの変更を取得（Git Directoryにのみ反映）。
git merge

ブランチを統合。
git gc

不要なデータを整理し、Git Directoryを最適化。
git fsck

Git Directoryのデータ構造をチェック。
