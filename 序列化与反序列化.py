import json
import base64
import pickle
import msgpack
# with open('e:/1/1.jpg',mode='rb')as f:
#     a=f.read()
    # print(type(a))
    # b=base64.b64encode(a)
    # print(type(b))
    # c=pickle.dumps(b)
    # print(type(c))
    #
    #
    # d=pickle.loads(c)
    # # print(d)
    # e=base64.b64decode(d)
    # print(e)
    # print(a == e)

# import json  # 不能直接序列化二进制
# import base64 # 编码成二进制，去除特殊符号

    # a=f.read()
#     print(type(a))              #类型：字节bytes
#     b=base64.b64encode(a)   #编码成二进制，去除特殊符号
#     print(b)
#     c=b.decode('ascii')   #把二进制转换成字符串，因为json不支持二进制序列化
#     d=json.dumps(c)     #jason序列化
#     print(d)
#
#     e=json.loads(d)     #json 反序列化
#     print(e)
#     f=e.encode('ascii')   #把字符串转换成二进制
#     print(f)
#     g=base64.b64decode(f)  #base64解码，恢复成原数据
#     print(g)
#     print(a==g)
# with open('e:/1/2.jpg',mode='wb')as f:
#     f.write(g)

# a={'name':'pp','age':22}
# json.dump(a,open('e:/1/11.txt','w'))
# b=open('e:/1/11.txt',mode='r')
# print(b.read())
# c=json.load(open('e:/1/11.txt','r'))
#
# print(c)

# list = ['Apple','Huawei','selenium','java','python']
# #   #把list先序列化，写入到一个文件中
# #  # 两步操作 1步先序列化 列表对象  2步把序列化成的字符串写入文件
# # json.dump(list, open('e:/test.txt','w'))
# # r1=open('e:/test.txt','r')
# # print(r1.read())
# # res=json.load(open('e:/test.txt','r'))
# # print (res)
# # print('数据类型:',type(res))
# dict = {'name':'zhangsan', 'age':33, 'address':'红星路'}
# print('未序列化前的数据类型为:', type(dict))
# print('为序列化前的数据：', dict)
# #对dict进行序列化的处理
# dict_xu = json.dumps(dict,ensure_ascii=False)    #添加ensure_ascii=False进行序列化
# print('序列化后的数据类型为：', type(dict_xu))
# print('序列化后的数据为：', dict_xu)
# #对dict_xu进行反序列化处理
# dict_fan = json.loads(dict_xu)
# print('反序列化后的数据类型为：', type(dict_fan))
# print('反序列化后的数据为: ', dict_fan)



stu = {
    'name': 'lili',
    'age': 18,
    'score': 100
}

# 序列化
msg_str = msgpack.packb(stu)
print(len(msg_str))
json_str = json.dumps(stu)
print(len(json_str))

# 反序列化
stu_dict = msgpack.unpackb(msg_str, use_list=False, encoding='utf-8')
print(stu_dict)