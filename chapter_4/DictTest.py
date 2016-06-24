#coding=utf-8
from copy import deepcopy

# 构造字典
list_test = [("name", "fupei"), ('age', 12), ("nums", ['23', 'fupei', 'op'])]
json = dict(list_test)
json2 = dict(name="fupei", lll="woqu")

print json2

json2.clear()
print json2

json3 = deepcopy(json)
print json
print json3

# 元数据的name不会被修改
json3['name'] = "wocao"
print json
print json3

# 元数据的name不会被移除
json3.pop("name")
print json
print json3

# 浅复制时，对jsonarray的操作应该会影响原数据
json3['nums'].remove('23')
print json
print json3

# 浅复制
# {'age': 12, 'name': 'fupei', 'nums': ['23', 'fupei', 'op']}
# {'age': 12, 'name': 'fupei', 'nums': ['23', 'fupei', 'op']}
# {'age': 12, 'name': 'fupei', 'nums': ['23', 'fupei', 'op']}
# {'age': 12, 'name': 'wocao', 'nums': ['23', 'fupei', 'op']}
# {'age': 12, 'name': 'fupei', 'nums': ['23', 'fupei', 'op']}
# {'age': 12, 'nums': ['23', 'fupei', 'op']}
# {'age': 12, 'name': 'fupei', 'nums': ['fupei', 'op']}
# {'age': 12, 'nums': ['fupei', 'op']}

# 深复制
# {'age': 12, 'name': 'fupei', 'nums': ['23', 'fupei', 'op']}
# {'age': 12, 'name': 'fupei', 'nums': ['23', 'fupei', 'op']}
# {'age': 12, 'name': 'fupei', 'nums': ['23', 'fupei', 'op']}
# {'age': 12, 'name': 'wocao', 'nums': ['23', 'fupei', 'op']}
# {'age': 12, 'name': 'fupei', 'nums': ['23', 'fupei', 'op']}
# {'age': 12, 'nums': ['23', 'fupei', 'op']}
# {'age': 12, 'name': 'fupei', 'nums': ['23', 'fupei', 'op']}
# {'age': 12, 'nums': ['fupei', 'op']}

# 不能加入这些key进去，为什么呢。。。。
json.fromkeys(['aaa', 'bbb', 'year'], "")
print json
# 后可以跟默认值
print dict.fromkeys(['aaa', 'bbb', 'year'], "")
print {}.fromkeys(['aaa', 'bbb', 'year'], "")

# 获取指定key 的 value，可以设置默认的值
print json.get("name2", "default")

print json.has_key("name")

# 更新
json_one = {"name":"fupei", "age":123}
json_two = {"age":99}
json_one.update(json_two)
print json_one
