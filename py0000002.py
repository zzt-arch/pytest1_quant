
# def test1():
#     global a
#     a=120
#     print(a)
# test1()
# print(a)
# def outer():
#     a=5
#     def inner():
#         nonlocal a
#         a=10
#         def inner1():
#             a=15
#             print(a)
#         inner1()
#         print(a)
#     inner()
#     print(a)
# outer()
# add=lambda a,b: a+b
# print(add(10,20))
# def pius(x,y):
#     return x*y
# print(pius(3,4))
# funa=lambda :"yini"
# print(funa())
# funa1=lambda nn:nn
# print(funa1('binbin'))
# funa2=lambda name='nihao',age=18:(name,age)
# print(funa2('goudan',30))
# funa3=lambda x,y,z=4:(x+y)**z
# print(funa3(1,2))
# funa4=lambda **lk:lk
# print(funa4(name='nihao',age=18))
# fu=lambda a,b:'a比b小'if a<b else"a大于等于b"
# print(fu(4,5))
# import builtins
# print(dir(builtins))
# print(abs(-13))
# print(sum((1,300)))
# print(int(sum((1.5,300))))
# print(min(1,3,9))
# print(max(1,3,9))
# li=['a','b','c']
# l=[1,2,3]
# print(list(zip(li,l)))
# for i in zip(li,l):
#     print(i)
# li=[1,3,5]
# fu=lambda x:x*5
# for i in map(fu,li):
#     print(i)
# from functools import  reduce
# li=[1,2,3,5]
# fu=lambda a,b: a+b
# print(reduce(fu,li))
# t=[1,3,5]
# a,*b=t
# print(a,b)
# def login():
#     pwd=input('Enter your password: ')
#     if len(pwd) >=6:
#         return "密码输入成功"
#     raise Exception('密码长度不足6位，请重新输入')
# try:
#     print(login())
# except Exception as e:
#     print(e)
# import pytest
# print(pytest.name)
# pytest.fu()
# from pytest import fu2,fu3,name
# fu2()
# fu3()
# print(name)
# from pytest import*
# print(age)
# import pytest as p
# p.fu()
# from pytest import fu as f,name,fu2 as f2
# f()
# print(name)
# f(2)
import pack_01
# def add():
#     s=0
#     for i in range(1,101):
#        s=s+i
#     print(s)
# add()
# def main(x):
#     if x==1:
#         return 1
#     return x+main(x-1)
# print(main(100))
# def fu(n):
#     if n <=1:
#         return n
#     return fu(n - 1) + fu(n - 2)
# print(fu(6))
# def outer(x=3):
#     y = 10
#     def inner():
#         print(x + y)
#     inner()
# outer()   # 不要 print
# def fu(x,y):
#     return x+y
# print(fu(2,4))
# def fu(m):
#     print(m)
#     def fu1(n):
#         print(n)
#         return m+n
#     return fu1
# o=fu(5)
# print(o(6))
# def fu1():
#     print('nihao')
# def fu2(fn):
#     print('zzt')
#     fn()
# fu2(fu1())
# def send1():
#     print('nihao1')
# def send2():
#     print('nihao2')
# def outer(f,g):
#     def inner():
#         print('登录i')
#         f(),g()
#     return inner
# o=outer(send1,send2)
# o()
# def outer(fn):
#     def inner():
#         print("inner function")
#         fn()
#     return inner
# @outer
# def send():
#     print("Hello world")
# send()
# def outer(fn):
#     def inner(name):
#         print(f'{name}是谁')
#         fn(name)
#     return inner
# @outer
# def foo(name):
#     print('woshizzt')
# foo('zzt')

