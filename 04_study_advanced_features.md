### 高级特性
#### 切片
`list[0:3]` ，从list的索引0开始，到索引3未知，不包括索引3，取出元素。即list[0], list[1], list[2], 也可以省略为 `list[:3]`  
省略冒号前面的数字，表示从索引0开始。省略冒号后面的数字，表示到索引到最后一位。  
如果冒号前后的数字超过list的最大数，则只会得到list的边界为止，不会超出边界，也不会报错。  
对list的切片得到的结果为list，对tuple的切片得到的结果为tuple
```python
# 取前10个，0～9
list[:10]

# 取后10个，倒数第10个～最后一个
list[-10:]

# 从 索引0 到 索引9 ，步进为2，0，2，4，8
list[0:10:2]

# 从头到尾，步进为5
list[::5]
```

#### 迭代
不仅list和tuple可以通过for进行遍历，dict也可以通过for循环进行遍历  
通过 `instance()` 方法可以判断一个对象是否可迭代  
通过 `enumerate()` 可以取出可迭代对象的下标，既可以通过类似Java的方式来进行遍历
```python
d = {'a': 1, 'b': 2, 'c': 3}

# 遍历key
for  key in d:
  print(key)

# 遍历value
for value in d.values():
  print(value)

# 判断是否可迭代
print(isinstance(d, Iterable))

# 通过下标进行遍历
l = [1, 2, 3, 4]
for index in enumerate(l):
  print(index)

```

#### 列表生成式
```python
# range()函数会生成从 1~9 的序列
print('range(1, 10): ', list(range(1, 10)))

# 对range()生成的序列做二次处理，将处理后的序列转为list
print([x * x for x in range(1, 10)])
print(list(x * x for x in range(1, 10)))

# 筛选range()生成的序列
print(list((x * x) + 1 for x in range(1, 10) if x % 2 == 0))
```
