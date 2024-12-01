＜c3m2で出てきたコマンド群まとめ＞

説明とリンク

git ブランチ

git branch を
使うと、ブランチの一覧表示や作成、削除を行うことができます。

git branch <名前> を使用します。

git branch <name>
を使うと、リポジトリに新しいブランチを作成することができます。

git branch -d <name> を使用します。

git branch -d <name>
を使うと、リポジトリからブランチを削除することができます。

git branch -D <name> を使用します。

git branch -D <branch>
は、ブランチを強制的に削除します。

git checkout <branch> はブランチを強制的に削除します。

git checkout <branch>
は現在の作業ブランチを切り替えます。

git checkout -b <new-branch>。

git checkout -b <new-branch> は
新しいブランチを作成し、それを現在の作業ブランチにします。

git merge <branch> を実行します。

あるブランチの変更を別のブランチに
マージ
します。

git merge --abort

git merge --abort
は、マージが衝突した場合にのみ使用できます。このコマンドはマージを中止し、マージ前の状態に戻そうとします。

git log --graph

git log --graph 
はコミットやマージの履歴を ASCII グラフで表示します。

git log --oneline

git log --oneline
は各コミットを一行で表示します。

git remote 

$ git remote
 allows you to manage the set of repositories or “remotes” whose branches you track.

git remote -v

$ git remote -v
 is similar to $ git remote, but adding the -v shows more information such as the remote URL.

git remote show <name>

$ git remote show <name>
 shows some information about a single remote repo.

git remote update

$ git remote update
 fetches updates for remotes or remote groups.

git fetch

$ git fetch
 can download objects and refs from a single repo, a single URL, or from several repositories at once.

git branch -r

$ git branch -r
 lists remote branches and can be combined with other branch arguments to manage remote branches.
