"""
建议40：深入掌握ConfigParser
"""

# 在suggestion33有提到这个使用
# 读取一个节点的所有项
from configparser import ConfigParser
conf = ConfigParser()
conf.read('test.cfg')
conf_dict = dict(conf.items('DEFAULT'))
print(conf_dict)
# {'version': '1.0', 'name': 'test', 'option': 'oFf', 'platform': 'windows'}

# getboolean()将配置项的值如0, false, no, off转换为布尔值False，而对应的1,true, yes, on则被转义为True，其他值会抛出ValueError异常
# false, no , off不限大小写
print(conf.getboolean('DEFAULT', 'option'))
# False

# 查找规则，如果读取的配置项不在指定的节点里时，ConfigParse将会到[DEFAULT]节点中查找。
# DEFAULT必须是全大写
# 查找规则：
# 1、如果找不到节点，抛出NoSectionError。
# 2、如果给定的的配置项出现在get()方法的vars参数中，则返回vars参数中的值。
# 3、如果在指定的节点中含有给定的配置项，则返回其值。
# 4、如果在[DEFAULT]中有指定的配置项，则返回其值。
# 5、如果在构造函数的defaults参数中有指定的配置项，则返回其值。
# 6、抛出NoOptionError。
print(conf.get('section1', 'platform'))
# windows


# 从配置里获取格式化后的数据库连接字符串
conf = ConfigParser()
conf.read('format.conf')
print(conf.get('db1', 'conn_str'))
print(conf.get('db2', 'conn_str'))
# mysql://aaa:ppp@(host)s:3306/example
# mysql://root:www@(host)s:3306/example

