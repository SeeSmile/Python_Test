#coding=utf-8

# 第二章 2.2内容

text = "wolldfnljhhhaaa"
# 简单打印
print text[1]   # o
print text[-6]  # h
print text[-5:-2]   # hha
print text[-3:]     # aaa
print text[:2]  # wo

# 步长
print text[2:9:2]
print text[::-1]
print text[4:0:-1]
print text[4::-1]

# in运算
text_in = "yezsIdoZ"
print 'yes' in text_in

print len(text_in)
print max(text_in)
print min(text_in)
