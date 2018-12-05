### 类
- \__init__ 函数函数相当于构造函  
- 所有类的方法的第一个参数都要是 `self` ，表示实例本身。因为在调用类方法的时候默认都会把实例自身作为参数传入
- \__xx，前面加了两个下划线的变量无法被外界访问，但是可以通过 `_obj__xx` 访问到，这是因为编译器强制修改了变量名    

```python
# 定义一个 Student 类，继承 object
class Student(object):
  # __init__ 相当于构造方法，第一个参数必需是 self 表示实例本身，后续的参数表示类的成员变量
  def __init__(self, name, age):
    self.name = name
    self.age = age

# 实例化 Student 对象的实例
s1 = Student()
```

#### 判断对象的类型
- type(obj)  
  返回对象的类型，只能判断本身的类型
- isinstance(obj, class)  
  返回 `True` 或者 `False` ，可以判断继承关系

types 模块
- types.FunctionType
- types.BuiltinFunctionType
- types.LambdaType
- types.GeneratorType

`dir()`  
获取一个对象的所有属性和方法  
其中的 `__xxx__` 方法都有特殊用途

`setattr(obj, attr, value)`  
设置对象的属性

`getattr(obj, attr)`  
设置对象的属性  

`hasattr(obj, attr)`  
是否有指定的属性  

#### __slots__
通过一下的方式可以给一个类添加额外的属性和方法  
```python
from types import MethodType

class Student(object):
    pass

s = Student()
# 为 实例 添加属性
s.name = 'lwtor'
print(s.name)

# 为 实例 添加方法
def say_hello(self):
    print('hello, I am %s' %(self.name))

s.say_hello = MethodType(say_hello, s)
s.say_hello()

# 为类添加方法和属性
Student.say_hello = say_hello
Student.name = ''

s2 = Student()
s2.name = 'allen'
s2.say_hello()
```

使用 `__slots__` 可以显示对类的属性，禁止添加其他的属性  
 `__slots__` 关键字只对当前类生效，对其子类不起作用
```python
class Animal(object):
  # 只能使用定义的属性
    __slots__ = ('name', 'age')
```

#### @property
对于一个类，可以直接对属性进行赋值，但是这样就可以赋值任意类型或者任意的内容。也可以使用 `setter` 的方式对赋值的内容进行约束，但是调用形式麻烦。  
通过 `@property` 关键可以对类的属性进行约束。同时，又可以通过属性进行赋值。  
 `@property` 的内部是通过装饰器实现的。  

通过 `@property` 相当于定义了一个类的一个属性的 `getter` 方法。  
通过 `@xxx.setter` 相当于定义了一个类的一个属性的 `setter` 方法  

```python
class Student(object):
    # 定义 score 参数，相当于 getter 方法
    @property
    def score(self):
        return self._score

    # 定义 score 参数的 setter 方法， 实例化的对象可以通过 studfent.score=xx 进行调用
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100 !')
        self._score = value

    s1 = Student()
    # 相当于 s1.score(10)
    s1.score = 10
```

#### 多继承
```python
def Cat(Animal, Runnable):
  pass
```

将功能性的类名命名为 `xxxMixIn` ，应该只是一种约定俗成的命名规则，暂未发现其他用处

#### 定制类
- \__str__ :  
  通过 `print` 打印对象信息，类似于 `toString()` 方法
- \__repr__ :  
  直接通过对象本身调用
- \__iter__ :  
  返回迭代对象。
- \__next__ :  
  由 `for` 调用，每次返回循环的下一个值
- \__getitem__ :  
  通过类似数组的方式，访问随机元素 `s[5]` ,如果需要使用 `切片` 则需要在方法内部做判断
- \__getattr__ :  
  当调用一个不存在的属性时，会试图通过该方法来尝试获取属性值
- \__call__ :
  通过对象本身进行调用

#### 枚举类
```python
from enum import enum
Month = Enmu('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
  print(name, '=>', member, ',', member.value)
```
