content = '''
Python3 高级开发工程师 上海互教教育科技有限公司上海-浦东新区2万/月02-18满员
测试开发工程师（C++/python） 上海墨鹍数码科技有限公司上海-浦东新区2.5万/每月02-18未满员
Python3 开发工程师 上海德拓信息技术股份有限公司上海-徐汇区1.3万/每月02-18剩余11人
测试开发工程师（Python） 赫里普（上海）信息科技有限公司上海-浦东新区1.1万/每月02-18剩余5人
Python高级开发工程师 上海行动教育科技股份有限公司上海-闵行区2.8万/月02-18剩余255人
python开发工程师 上海优似腾软件开发有限公司上海-浦东新区2.5万/每月02-18满员
'''
#
import re
for one in  re.findall(r'([\d.]+)万/每{0,1}月', content):
    print(one)

import copy

list1 = [1, 2, [3, 4]]

b = copy.deepcopy(list1)

print("修改前的list1:", list1)
print("list1原地址:", id(list1))
print("list1的深拷贝地址b:", id(b))
print("============修改原对象的值===================")
list1[1]= 5
print("修改后的list1:", list1)
print("list1修改后的地址:", id(list1))
print("修改后的list1，深拷贝的a:", b)
print("list1修改后的深拷贝地址a:", id(b))


a = [1,2,3,None,(),[],]

print(len(a))
print(a[5])
b=[1,2,3,]
print(len(b))
f=open()