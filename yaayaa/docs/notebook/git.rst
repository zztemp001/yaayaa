git 使用
********

设置
====

.. code-block::

    prompt> git config --global user.name "zwm"
    prompt> git config --global user.email "zwm@gmail.com"

    # 将命令行界面设置为彩色
    prompt> git config --global color.ui "always"

分支
====

.. code-block::

    # 基于 master 分支创建名为 new 的新分支，然后使用 checkout 切换至 new 分支
    prompt> git branch new
    prompt> git checkout new

    # 基于 master 分支创建名为 alternate 的新分支并直接切换至新分支
    prompt> git branch -b alternate master

    # 将分支 alternate 中的修改历史全部合并至 master 分支
    prompt> git checkout master
    prompt> git merge alternate

    # 将分支 contact 中的修改历史压缩成一次提交，然后合并至 master 分支
    prompt> git checkout master
    prompt> git merge --squash contact

    # 删除名为 about2 的分支
    prompt> git branch -d about2

    # 将 about 分支重命名为 aboutme
    prompt> git branch -m about aboutme

历史
====

.. code-block::

    # 显示历史提交信息
    prompt> git log

    # 显示最近5条提交历史信息
    prompt> git log -5



冲突处理
========

手工解决。或使用可视化的 diff 工具解决。 ::

    prompt> git mergetool

压缩和清理版本库，但不改变版本库的提交历史，用于优化性能 ::

    prompt> git gc

导出版本库为压缩文件，不包含历史记录 ::

    prompt> git archive --format=zip --prefix=mysite-release/ HEAD > mysite-release.zip
    prompt> git archive --format=tar --prefix=mysite-release/ HEAD | gzip >mysite-release.tar.gz

