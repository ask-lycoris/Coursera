mergeには複数種類があるっぽいんでそれをここにまとめる。

Fast-forward merge:

A fast-forward merge does not create a new merge commit. Instead, it moves the pointer of the branch forward to the latest commit because there are no diverging changes.

Squash on merge:

A squash merge combines all the changes from a branch into a single commit, but it does not create a merge commit that shows the branch history.

Three-way Merge (3-way Merge) の説明
Three-way merge は、Gitが分岐したブランチを統合する際に使用される、最も一般的なマージ手法の1つです。3つの「スナップショット」を比較して、変更内容を統合します。

1. Squash on Merge
Squash on Merge は、複数のコミットを1つのコミットにまとめてからブランチを統合するマージ方法です。

特徴
複数のコミットを1つにまとめる

開発中に作成された細かいコミット（例: "Fix typo", "Add comments" など）を1つのコミットに統合します。
統合したコミットに対して、新しいコミットメッセージを設定可能。
履歴がシンプルになる

プロジェクト全体の履歴をクリーンで見やすくするために使用されます。
開発ブランチの詳細な履歴は保存されません。
動作例
# feature ブランチを main ブランチに squash merge
git checkout main
git merge --squash feature
git commit -m "Summarized feature changes"
すべての変更が main に統合されますが、feature の個々のコミット履歴は失われます。
利用する場面
開発ブランチに細かいコミットが多い場合:
細かい変更を履歴に残す必要がなく、統合後の履歴を簡潔にしたい場合。
コードレビュー後の統合:
レビューが完了したブランチを統合する際に使われます。
2. Fast-Forward Merge
Fast-Forward Merge は、履歴が線形である場合にのみ使用されるシンプルなマージ方法です。

特徴
新しいコミットを作成しない

git merge コマンドを実行すると、現在のブランチのHEADポインタが統合先の最新コミットに移動します。
新しいマージコミットは作成されません。
履歴が線形に保たれる

履歴に分岐やマージコミットが発生せず、一連の直線的な履歴として残ります。
動作例
# main ブランチにチェックアウト
git checkout main

# feature ブランチを fast-forward merge
git merge feature
feature に新しい変更が追加されていても、分岐していない場合はそのまま main に統合され、HEADが移動します。
利用する場面
直線的な履歴を保ちたい場合:
チーム内で分岐やマージコミットを最小限に抑え、シンプルな履歴を好む場合。
ブランチ間に競合がない場合:
現在のブランチが完全に更新されている場合に使用。

Squash on Merge:
開発ブランチで細かくコミットしたが、メインブランチにはシンプルな履歴を残したい場合。
Fast-Forward Merge:
小規模な変更や履歴がすでにシンプルな場合に適しています。




＜Three-way Merge の動作原理＞
3つのスナップショットを使用:

共通の祖先（Base commit）: ブランチが分岐する前の共通のコミット。
現在のブランチのHEAD: 現在作業中のブランチの最新コミット。
統合する対象ブランチのHEAD: マージする相手のブランチの最新コミット。
これらの3つのスナップショットを比較し、差分を計算します。

マージの手順:

Gitは共通の祖先（Base commit）と各ブランチの変更を比較して、差分を統合します。
自動的に統合可能な部分をマージしますが、競合（コンフリクト）がある場合は手動で解決する必要があります。
Three-way Merge の特徴
新しいマージコミットを作成:

マージの結果として、新しい「マージコミット」が作成されます。
このコミットには、どのブランチが統合されたかの情報が含まれます。
ブランチの履歴が保持される:

マージされたブランチの変更履歴を完全に残すため、変更の追跡が容易。
