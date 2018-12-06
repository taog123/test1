import re
# s='''mr5@163.com
# web.mr5@hotmail.com
# mr5@gmail
# mr5@google@baidu
# '''
# #
# a=re.findall('^m\w+\W+\S+',s)
# print(a)

# s="<a herf='www.mr5.com'>xu yu is ha pi</a>"

# a=re.compile("(?<=<a herf='www.mr5.com'>).*(?=</a>)")
# print(a.findall(s))
# a=re.findall("(?<=<a herf='www.mr5.com'>).*(?=</a>)",s)
# print(a)
# a=re.findall("(?<=>).*(?=<)",s)
# print(a)
s='''http://www.aliyun.com/index.html
https://login.mr5.com
mail:jack@hotmail.com
<username>xu yu</username>
ftp:///etc/sysconfig
'''

# regix=re.compile(r"(?P<key>\bh.*[s,p]\b)://(?P<value>.*)",re.M)
# result=regix.findall(s)
# print(result)
# a=re.findall(r"(?P<key>\bh.*[s,p]\b)://(?P<value>.*)",s,re.M)
# print(a)
a=re.findall(r"(?P<key>\w+)://(?P<value>.*)",s,re.M)
print(a)