[TOC]

### 1.版本控制工具
    git 分布式,没有中央服务器(每个节点都是中央服务器) 
    svn 集中式,必须有一个中央服务器

### 2.GIT
    配置:
    系统级配置: git config --system [选项]
    $ git config --system user.name tarena
    $ sudo git config --system user.name tarena
    会在/etc下创建一个 gitconfig 的配置文件
    > cat /etc/gitconfig 
```
[user]
	name = tarena
```
    全局配置:git config --global [选项]
    > git config --global user.email 42737521@qq.com
    会在~/下创建一个 .gitconfig 的隐藏配置文件
    > cat ~/.gitconfig 
```
[user]
	email = 42737521@qq.com
```




