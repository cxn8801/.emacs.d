我的emacs配置文件

magit
(global-set-key (kbd "C-x g") 'magit-status)
C-x g来查询状态
会打开一个buffer，显示
Head: //指向当前分支的的最近一次提交
Merge: //远程分支的最近一次提交
Untracked files //工作区中有，但没有加入git管理
Unstaged files //git管理的，在工作区已经修改的，但是没有用git add进入staged状态

S stages all files
alt+x magit-status
c c 输入commit内容 ctrl+c ctrl+c 提交commit
magit 快捷键 Pu push

b b 改变当前分支