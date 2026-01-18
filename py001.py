
print("hello brother")
# bug
# print("hello world")
print(123)
# '''
# woshi
# '''
# """
# dddddd
# """/
print('哈哈哈','卧槽',sep='。')
print('hello',end='$$')
print('[]')
pi1=9
pi2=89
total=pi1+pi2
print(total)
print(pi1,pi2,sep='$$')
a=999
print(a)
b='111'
a=520
print(b,a,sep='，')
er_1=9.9
print(type(er_1))
print(type(True))
print(type(False))
print(True+False+True)
ka=8+8j
ka2=6-4j
print(ka+ka2)
name='01'
age=20.0958794
print("wodemingzishi:%s"%name)
print("年龄是:%d"%age)
print('我的名字是：%s,年龄是:%s'% ( name,age))
print('%.6f'%age)
print("我是你的%s%%"%age)
name='涛涛'
(age)=20
print(f'我的名字是{name}',f'我今年{age}岁啦！')
print(5%2)

print(1+90/2**6)
nm1=23
nm2=90
nm1+=nm2
print(nm1)
a=2
a+=1
print(a)
print('股票代码\t成交量\t市值')
n1=20.89
print(f'我是你的{n1}%\n你知道吗？')
print('2005-10-05')
score=126
if 85<=score<=100:
    print('优秀')
elif 60<=score<85:
    print('良好')
elif 0<=score<60:
    print('不及格')
else:
    print('分数无效')
ticket=True
temp=56
if ticket==True:
    print('可进站',end=' ')
    if 36.5 <= temp <= 38.0:
        print('体温正常')
    elif 38.0<temp<=42.0:
        print('你需要去医院')
    else:
        print('请输入正确的体温数值')
else:
    print('不让进')
i=1
s=0
while i<=100:
    s=s+i
    i=i+1
print(s)
i=1
while i<=3:
    print(f'外循环{i}次')
    i = i + 1
    j=1
    while j<=5:
        print(f'内循环{j}次')
        j = j + 1
i="hellopython"
for a in i:
    print(a)
s=0
for i in range(1,101):
     s=s+i
print(s)
i=1
while i<=5:
    print(f'吃{i}个苹果')
    if i==3:
        print(f"第{i}个苹果不好吃")
        i = i+1
        continue
    i=i+1
for i in range(1,100):
    print(f'吃{i}个苹果')
    if i==56:
        print(f'第{i}个苹果不好吃')
        i = i+1
        continue
    i=i+1
i=1
for i in range(1,4):
    print(f'外循环{i}次')
    i = i + 1
    j=1
    for j in range(1,6):
        print(f'内循环{j}次')
        j = j + 1
a="hello"
el=a.encode()
print(el)
print(type(el))
w=el.decode()
print(w)
print(type(w))
print("ty"+'rt')
print('你好\n'*10)
name='11'
print('1'and'0'in name)
name='symbol'
print(name[-2])
for a in range(1,10):
    print(a)
fk="abcdefghijk"
print(fk[0:7])
print(fk[4:-1])
print(fk[-5:-1])
print(fk[-1::-1])
print(fk[-1:-6:-1])
name='symmmmbol'
print(name.find('y'))
print(name.find('b'))
print(name.index('y'))
print(name.count('m',6))
print(name.startswith('m'))
print(name.endswith('l'))
while True:
    print('1')
    break
name='symmmmbol'
print(name.find('y'))
print(name.find('b'))
print(name.index(''))
i=5
for a in range(1,i):
    print(a)
