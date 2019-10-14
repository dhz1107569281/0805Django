# import re
#.匹配非换行符的任意字符
# strings='hello world \n I am your firend_Tom \t I am 180 years old'
# ret=re.findall(r'.',strings)
# print(ret)

# \d 匹配数字
# strings='hello world \n I am your firend_Tom \t I am 180 years old'
# ret=re.findall(r'\d',strings)
# print(ret)

# \D 匹配非数字
# strings='hello world \n I am your firend_Tom \t I am 180 years old'
# ret=re.findall(r'\D',strings)
# print(ret)

# \w 匹配数字,字母,下划线
# strings='hello world \n I am your firend_Tom \t I am 180 years old'
# ret=re.findall(r'\w',strings)
# print(ret)

# \W 匹配非数字,字母,下划线
# strings='hello world \n I am your firend_Tom \t I am 180 years old'
# ret=re.findall(r'\W',strings)
# print(ret)

# [] 匹配中括号中的任意一个元素
# strings='hello world \n I am your firend_Tom \t I am 180 years old'
# ret=re.findall(r'[hlo ]',strings)
# print(ret)

#^ 取反，可以和中括号一起使用
# strings='hello world \n I am your firend_Tom \t I am 180 years old'
# ret=re.findall(r'[^hlo]',strings)
# print(ret)

#()组匹配 ，将组外的匹配条件作为条件匹配，返回组内匹配到的内容
# strings='hello world \n I am your firend_Tom \t I am 180a years old'
# ret=re.findall(r'(\d)\w',strings)
# print(ret)

#()命名组 ?P<名称>
# strings='hello world \n I am your firend_Tom \t I am 180a years old'
# ret=re.findall(r'(?P<hello>\d)\w',strings)
# print(ret)

#*匹配任意多个，匹配零次或多次
# strings='hello world \n I am your firend_Tom \t I am 180a years old'
# ret=re.findall(r'.*',strings)
# print(ret)

#+匹配1次或多次
# strings='hello world \n I am your firend_Tom \t I am 180a years old'
# ret=re.findall(r'.+',strings)
# print(ret)

#?匹配0次或1次
# strings='hello world \n I am your firend_Tom \t I am 180a years old'
# ret=re.findall(r'.?',strings)
# print(ret)

#{} 匹配指定次
# strings='hello world \n I am your firend_Tom \t I am 180a years old'
# ret=re.findall(r'.{3}',strings)
# ret=re.findall(r'.{2,3}',strings)
# print(ret)

#^
#开始
# strings='hello world \n I am your firend_Tom \t I am 180a years old'
# ret=re.findall(r'^.{3}',strings)
# print(ret)

#$ 结尾
# strings='hello world \n I am your firend_Tom \t I am 180a years old'
# ret=re.findall(r'.{3}$',strings)
# print(ret)

import re
# re.findall()匹配所有满足正则的条件的字符
string='this is my f_ck\n 123ds\ta'
# ret=re.findall(r's',string)
# print(ret)
# ret=re.findall(r'.',string)
# print(ret)
# ret=re.findall(r'\d',string)
# print(ret)
# ret=re.findall(r'\D',string)
# print(ret)
# ret=re.findall(r'\w',string)
# print(ret)
# ret=re.findall(r'[\d]',string)
# print(ret)
# ret=re.findall(r'(\d)',string)
# print(ret)
# ret=re.findall(r'(\d)\w',string)
# print(ret)
