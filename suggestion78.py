# coding: utf-8
"""
建议78：将包发布到PyPI

利用建议72条的pastescript生成安装包后，利用setuptools打包成zip或者tar
sudo python3 setup.py sdist --formats=zip,gztar

setuptools的sdist命令的意思是构建一个源代码发行包，产生的包文件放在./dist目录下

下游开发者收到后有两种安装方式：一种是解压缩，进入setup.py文件所在的目录执行 python3 setup.py install 命令安装；
另一种是使用pip安装，执行 pip3 install xxx.tar.gz 即可。删除已安装的库可以用pip uninstall xxx
"""
