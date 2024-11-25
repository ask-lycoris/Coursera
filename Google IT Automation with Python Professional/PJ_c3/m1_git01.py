### Fundamental git architecture concepts
# local repository: Gitは分散型バージョン管理システムであり、各ユーザーは自分のローカルリポジトリを持っています。このローカルリポジトリには、プロジェクトの全てのファイルの履歴が保存されています。
# staging area: A file maintained by Gitthat contailns all of theinfomation about what files and changes are going to go into your next commit.
# git addコマンドを使用して、変更をステージングエリアに追加します。これにより、どの変更を次のコミットに含めるかを指定します。
# commit: git commitコマンドを実行すると、ステージングエリアにある変更がローカルリポジトリにコミットされます。この際、コミットメッセージを指定することで、その変更内容を説明することができます。
# remote repository: もし、リモートリポジトリ（例えばGitHubやGitLabなど）に変更を反映させたい場合は、git pushコマンドを使用します。これにより、ローカルリポジトリのコミットがリモートリポジトリにアップロードされます。

# Gitは主に3つの要素から構成されている。
# Git directory： すべてのファイルと変更の履歴を保持
# Working tree: 私たちが行った変更を含む、プロジェクトの現在の状態が保持
# Staging ara： 次のコミットに含まれる変更を保持
# Gitを使用しているからと言ってすべてが履歴に反映されるわけではない。track/ untrack でファイルを管理している。

git config --global user.email "me@example.com"
git config --global user.name "My name"

# Add file changes on git repository staging area.
git add disk_usage.py 
# Check current status of local git repository.
git status

# Commit the chaneges you did previously to the local repository.
git commit                                  # ---> after this, the editor will be open, so if you add commit message on just one liner, do underbelow.
git commit -m "Your commit message here"    # This can add also commit messages and 

# The git directory contains all the changes and their history and the working tree contains the current versions of the files.
