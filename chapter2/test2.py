# __hash__,__eq__函数
# 如何__hash__=None ,则对象是可变对象
# __eq__ 等价于==
# 这俩个函数的内部逻辑可以自己重载

# __bool__() 方法，一般默认bool()时返回True的
x= object()
print(bool(x))

# __bytes__()方法，基本的object类没有定义这个方法，意味着所有的类默认是没有提供这个方法的，
# 所以，想要将对象序列化为不可变字符串，需要自己实现这个方法
# 然后自己写从字节创建对象的函数

