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

##### sorted()函数
排序  
对于字符则比较其ASCII的大小  

- 参数：  
 - key：先作用于每一个元素，根据结果进行排序，根据排序输出原始元素
 - reverse：是否倒序

#### 返回函数
将函数作为返回值  
通过一个函数，返回另一个函数，在外层函数中的变量可以被返回的函数使用，因为在返回内部的函数时，相关的变量都已经被保存到返回函数中了，这就叫 `闭包`  
返回函数并不会立即被执行，只有进行调用后才会执行函数  

#### 装饰器
装饰器decorator就是一个返回函数的高阶函数  
```python
def log(func):
    print('log', func)
    @functools.wraps
    def wrapper(*args, **kw):
        print('call %s()' %(func.__name__))
        return func(*args, **kw)
    return wrapper

@log
def func():
  pass
```

上面的代码，为 `func` 函数设置了适配器 `log` , 这样在调用 `func` 函数的时候，其实真正调用的是 `log` 函数，而 `log` 接受的就是一个函数，并返回 `wrapper` 函数，所以其实最后被调用的就是 `wrapper` 函数。相当于执行了 `log(func)()` ，这里的 `log(func)` 其实就是 `wrapper` 函数本身  

如果需要向装饰器传递参数，只需要在装饰器上嵌套多一层，也就是装饰器本身返回的是另一个装饰器，但是这样在使用 `@` 的时候稍有不一样，以为 `@` 后面的装饰器应该是一个接受函数作为参数的函数  

如果在使用装饰器时候，修改了原来函数名的指向，原本的函数名就不再指向最初的函数了，这个时候函数的 `__name__` 字段就会被改变了，如果不希望被改变，可以使用 `functools.wraps` 装饰器来修饰返回的函数  

#### 偏函数
`functools.partial`  
返回一个预先设定好某些参数的指定函数  
```python
from functools import partial

# 创建一个输出一条分割线的函数
print_line = partial(print, '------------------------')

# 创建一个分隔符为 * 的 print 函数
p_start = partial(print, sep='*')
```
