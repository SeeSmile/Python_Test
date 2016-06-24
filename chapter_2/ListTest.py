#coding=utf-8
list_test = ["fupei", "lili", "fupei", "xiaohong", "wocao", "234"]

# list的分片
name = list("wohaishi") #['w', 'o', 'h', 'a', 'i', 's', 'h', 'i']
print name

# 理解为替换操作
# list_test[1:4] = []
print list_test[::-1]
print list_test + ["sdfjl", "sdlfjewf"]

list_app = ["sdflj", "sldfuowet"]

# 追加一个
list_test.append(list_app)

# 切片的追加
list_test[len(list_test) : ] = list_app
print list_test

# 追加多个
list_test.extend(list_app)
print list_test

# 统计(精准)
print list_test.count("fu")

# 没找到会引发异常
print list_test.index("fupei")

# 指定位置插入
list_test.insert(2, "two")
print list_test

# 移除指定位置的元素，并返回值
list_test.pop(-1)
print list_test

# 移除第一个匹配到的元素
list_test.remove("fupei")
print list_test

# 排序
list_sort = list_test[:]
list_sort.sort()
print list_sort

