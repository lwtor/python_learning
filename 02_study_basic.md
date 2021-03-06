### 指定编码
在 `.py` 文件的加入 `# -*- coding: utf-8 -*-`

### 字符串的相关方法
- `ord('str')` --> 获取字符的整数表示
- `chr('str')` --> 将整数转换成对应的字符
- `str.encode('coding')` --> 将字符装换成对应的编码
- `len('str')` --> 获取字符的字节数

### 格式化
使用 `%？` 作为占位符，与C类似， `%d` 表示整数， `%s` 表示字符串， 替换的内容使用 `%()` 包含起来。例如 `print('%s %d' %('hello', 100))`  
如果想要%作为普通字符输入，使用 `%%`  
也可以使用 `format()` 方法，替代{0}, {1}..等  
`print('{0} {1}'.format('hello', 'world'))`

### list
```python3
  # 初始化
  list = [1, 2, 3]

  # 随机访问
  a = list[0]
  # 获取最后一个元素，-2表示倒数第二个元素，如此类推
  last = list[-1]

  # 在末尾添加元素
  list.append(4)
  # 插入指定位置
  list.insert(1, 'new')

  # 删除末尾元素
  list.pop()
  # 删除指定位置
  list.pop(1)

  # 空列表       
  empty_list = []

  # 获取长度
  length = len(list)

```

### tuple

- 初始化之后不可修改
- 没有append(),insert()方法

```python
list = (1, 2, 3)

# 空tuple
empty_list = ()

# 这里只是定义了一个num变量，值为1，num并不是tuple
# 这里的括号表示数学中的小括号
num = (1)
# 定义一个只有一个元素的tuple
one_list = (1,)

# 下面的代码是可行的，因为修改的只是tuple中第三个元素的指向的list中的值，并没有改变tuple的值
list = (1, 2, ['A', 'B'])
list[2][0] = 'X'
list[2][1] = 'Y'

# 随机访问，与list类似，-1表示倒数第一个元素
a = list[0]
b = list[-1]

```

### 条件判断语句
```
if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
else:
    <执行4>
```

条件判断中不仅可以是Boolean，还可以是 `非零数值` 、 `非空字符串` 、 `非空list` 等，这些会被判断为True，否则为False

### input
使用 `input()` 方法获取到的值的类型为字符串类型。  
如果需要把字符串类型转成整形，可以通过 `int()` 方法

### 循环
#### for
```python
# 便利list或者tuple
for x in list:
  print(x)

for num in [1, 2, 3, 4, 5]:
  print(num)

# range()方法用于生成序列, 下面会生成 0~9 的序列
for i in range(10)
  print(i)
```
#### while
```python
while x < 10:
  print(x)
  # python不支持 x++ 操作，只能使用 x += 1 或者 x = x + 1
  x += 1
```

### dict
```python
num_dict = ['a': 1, 'b': 2, 'c': 3]

# 随机访问
x = num_dict['a']

# 判断是否存在key
‘a’ in num_dict
# 通过get()方法获取，如果key不存在返回None，也可以指定返回值
num_dict.get('a')
num_dict.get('a', -1)

# 通过key删除
num_dict.pop('a')

# key值必须是不可变的对象
```

### set
set中的值不可重复
```python
s = set([1, 2, 3])

# 添加
s.add(4)

# 删除
s.remove(4)

# 交集
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s1 & s2


```
