### 函数式编程
允许把函数本身作为参数传入另一个函数中，允许返回一个函数， `Python不是纯函数式编程语言`。  
常见的函数式编程语言： `cojure` , `scala` , `Haskell`  
编程语言的三种类型： `命令式编程` , `函数式编程` ， `逻辑式编程`

#### 高阶函数
- 变量可以指向函数
- 函数名也是变量
- 可以接受另一个函数作为变量

##### map()函数
接收两个参数，一个是 `函数` ，一个是 `Iterable`  
将传入的函数作用于序列中的每一个元素，并将结果作为一个新的 `Iterator` 返回  
```python
def func(x):
  return x * x
l = range(1, 11)
print(list(map(func, l)))
# 相当于 [func(x) for x in l]
```

##### reduce()函数
接收两个参数，一个是 `函数` ，一个是 `Iterable` , `函数` 必须为接受接收两个参数  
将结果连续和序列的下一个元素做累积计算   
`reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)`  
使用 `reduce()` 函数，需要引入 `functools` 包  

```python
from functools import reduce

def func(x, y):
    return x + y

l = list(range(1, 11))
print(l)
print(reduce(func, l))
```

##### filter()函数
接收一个函数和一个序列  
将装入的函数作用于每一个元素，根据返回值是 `True` 还是 `False` 决定保留还是丢弃该元素  
通过 `filter()` 方法得到的 `generator` 惰性序列，添加到惰性序列中的函数不会立即被执行，只有通过next()方法时，惰性序列才会去执行其中的函数，由于 `filter()` 方法得到的是一个惰性序列，如果在对这个惰性序列使用 `filter()` 方法，相当于增加多一个过滤器，这样在获取该惰性序列的元素的时候，会通过添加的过滤函数来判断是否返回该元素  
实现打印1000以内素数，如果能够实现该功能，表示基本掌握了 `filter()` 方法和惰性序列了
```python
def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
```
