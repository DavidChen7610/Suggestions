# coding: utf-8
"""
建议72：做paster创建包

打包项目放在setup中
设置打包y文件 setup.py
运行打包安装 python3 setup.py install
如果要删除已安装文件，到 /usr/local/lib/python3.5/dist-packages 手动删除文件即可

arithmetic只是一个示例性的小项目，所以setup.py文件非常简单。实际上若要把包提交到PyPI，需要
给出足够多的元数据才行。
首先安装pastescript
paster --help
paster help create
paster create -o setup-2 -t basic_package arithmetic
简单地填写几个问题以后，paster就在setup-2目录生成了名为arithmetic的包项目
setup-2
└── arithmetic
    ├── arithmetic
    │   ├── __init__.py
    │   └── __pycache__
    ├── arithmetic.egg-info
    │   ├── dependency_links.txt
    │   ├── entry_points.txt
    │   ├── not-zip-safe
    │   ├── PKG-INFO
    │   ├── SOURCES.txt
    │   └── top_level.txt
    ├── setup.cfg
    └── setup.py

创建公司项目，最好使用模板来生成配置信息
模板信息可以通过paster create --list-variables来查看
模板样板
[pasterscript]
description = corp-prj
license_name = abc
keywords = Python
long_description = corp-prj
author = xxx corp
author_email = xxx@example.com
url = http://example.com
version = 0.0.1

然后用以下命令生成安装包
paster create -t basic_package --config="corp-prj-setup.cfg" arithmetic  # 如果没有配置文件，自动生成文件，但需要手动输入一次即可
arithmetic
├── arithmetic
│   ├── arithmetic.py
│   ├── __init__.py
│   └── __pycache__
├── arithmetic.egg-info
│   ├── dependency_links.txt
│   ├── entry_points.txt
│   ├── not-zip-safe
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   └── top_level.txt
├── setup.cfg
└── setup.py

需要编写的库放入arithmetic包中，与__init__.py并列
python3 setup.py install后
在ipython3中就能引用arithmetic库，arithmetic模块
这种打包方式与之前的简单例子不同
若删除库，同上
"""
