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
