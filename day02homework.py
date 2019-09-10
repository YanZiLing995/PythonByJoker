#1.
import math
a = float(input('输入五边形顶点到中心的距离：'))
s = 2 * a *(math.sin (math.pi/5))
area = 5 * s * s /(4 * math.tan(math.pi/5))
print('五边形面积为：%.2f' %area)

#2.
import math
x1,y1 = eval(input("请输入点1的经度和纬度") )
x2,y2 = eval(input("请输入点2的经度和纬度"))
radius = 6371.01
 #math.radians()函数将度数转换成弧度数
x11 = math.radians(x1)   
y11 = math.radians(y1)
x22 = math.radians(x2)
y22 = math.radians(y2)
d = radius * math.acos(math.sin(x11) * math.sin(x22) + math.cos(x11) * math.cos(x22) * math.cos(y11-y22))
print('两点之间的大院距离为%5.8f km' %d )

#3.
import math
s = float(input('输入边长:'))
area = (5*s*s )/(4 * math.tan(math.pi/5))
print('面积为：%.6f' %area)

#4.
import math
n = int(input('边数：'))
s = float(input('边长：'))
area = (n *s *s )/(4 * math.tan(math.pi/n))
print ('面积为：%.6f' %area )

#5.
z = int(input('请输入ascii值'))
print( z , " 对应的字符为", chr(z))

#6.
name = input('输入名字：')
time = float(input('一周工作的时间：'))
hourmoney = float(input('每小时报酬'))
lks = float(input('联邦扣税率'))
zks = float(input('州预扣税率'))
Federal = time * hourmoney * lks
State = time * hourmoney * zks
Gross = time * hourmoney
NetPay = time * hourmoney - Federal - State
Total = Federal + State
print('name',name)
print('Time:%.2f' %time)
print('pay:%.2f' %hourmoney)   
print('GrossPay:%.2f' %Gross)
print('Federal :%.1f ' %Federal)
print('state :%.2f' %State)
print('Total :%.2f' %Total)
print('NetPay:%.2f' %NetPay)

#7.
num1 = input('输入一个整数')
print('颠倒后为：' ,num1[::-1])

# 7.19
1.
import math
a =float(input('a='))
b =float(input('b='))
c =float(input('c='))
d = (b * b)-( 4 * a * c)
if d>0:
    x1=(-b+math.sqrt(d))/(2*a)
    x2=(-b-math.sqrt(d))/(2*a)
    print('有两个根为：%0.6f 和%0.6f' %(x1,x2))
elif d== 0:
    x1=x2=(-c)/b
    print('有一个根为：%0.2f' %x1)
else:
    print('没有根')

#2.
import random
num1 = random.randint(1,100)
num2 = random.randint(1,100)
print(num1,num2)
sum = int(input('请输入两个整数的和'))
if sum == num1 +num2:
    print('True')
else:
    print('False')

#3.
today = int(input('今天是一周内的哪一天的数字（0-6）：'))
since = int(input('今天到未来某天的天数：'))
future = (today + since) % 7
if future == 0:
    print('星期日')
elif future == 1:
    print('星期一')
elif future == 2:
    print('星期二')
elif future == 3:
    print('星期三')
elif future == 4:
    print('星期四')
elif future == 5:
    print('星期五')
else:
    print('星期六')
print('今天为%d' %future)

#4.
# 升序显示
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
if a >= b:
    if a >=c:
        if b >=c:
            print('c,a,b')
        else:
             print('b,c,a')
    else:
        print('b,a,c')
else:
    if a >=c:
        print(c,a,b)
    elif b >= c:
        print(a,c,b)
    else:
        print(a,b,c)

#5.
kga =int(input('第一种kg:'))
paya =float(input('第一种pay:'))
kgb =int(input('第二种kg:'))
payb =float(input('第二种pay:'))
if kga >kgb:
    if paya < payb:
        print('第一种更好')
    else:
        print('第二种更好')
else:
    if paya > payb:
        print('第二种')
    else:
        print('第一种')

#6.
year = int(input('年：'))
month = int(input('月：'))
a = [1,3,5,7,8,10,12]
b = [4,6,9,11]
if month in a:
    print('有31天')
elif month in b:
    print('有30天')
else:
    if year % 400 ==0 :
        print('有29天')
    else:
        print('有28天')

#7.
import numpy as np
computer = np.random.choice(['正','反'])

#print(computer)

User = input('请输入[正/反]')
if computer == User :
    print('正确')
else:
    print('错误')

#8.
import numpy as np
computer = np.random.choice(['0','1','2'])
#print(computer)
User = input('请输入[0（石头），1（剪刀），2（布）]')
if computer == User :
    print('平局')
elif computer == '0' and User == '1':
    print('你输了')
elif computer == '1' and User == '2':
    print('你输了')
elif computer == '2' and User == '1':
    print('你输了')
else:
    print('你赢了')

#9.**
year = int(input('年：'))
month = int(input('月(1-12)：'))
day = int(input('天(1-31):'))
k = year % 100
j = year / 100
h = (day + (26*(month + 1)/10) + k + (k/4) + (j/4) + 5*j) % 7
print('今天为星期%d' %h)

#10.
import numpy as np
card = np.random.choice(['Acc','2','3','4','5','6','7','8','9','10','Jack','Queen','King'])
follower = np.random.choice(['梅花','红桃','方块','黑桃'])
print(card,follower)

#11.
num = input('输入一个数:')
a1 = num[2]
a2 = num[0]
if a1 == a2:
    print('是回文数')
else:
    print('不是回文数')

#12.
a,b,c =eval(input('输入三角形三边：'))
if a+b>c and a+c>b and b+c>a:
    d=a+b+c
    print('是合法的,周长为:%d' %d)
else:
    print('不是合法的')


#1.**
count1 = 0
count2 = 0
sum = 0
num = int(input('请输入整数'))
while num != 0:
    if num > 0:
        count1 +=1
    else:
        if num != 0 :
            count2 +=1
    sum =sum +num 
    num = int(input('请输入一个整数：'))
count = count1 +count2
if count !=0:
    avg = sum/count
    print('负数个数为%d,正数个数为%d,和为%d,平均值为%.2f' %(count2,count1,sum,avg))


#2.**
n = 10000
sum =0
for i in range(1,14):
    n = n * 0.05 + n
    if i ==10:
        print('十年后的学费是：%d' %n)
    if i>9:
        sum += n 
print('十年后大学四年的学费是：%d' %sum)

#4.
a = 0
for i in range(100,1001):
    if i % 5 == 0 and i % 6 == 0 :
        a +=1
        print(i,end='\t')
        if a % 10 ==0:
            print('\n',end='')

#5
n = 0
m = 0
while n*n <=12000:
    n += 1
print('n的平方大于12000的最小整数n为：%d' %n)
while m*m*m < 12000:
    m += 1
print('n的立方大于12000的最大整数n为：%d' %(m-1))

#7.
a = 0
b = 0
for i in range(1,50001):
    a +=1/i
for i in range(50000,0,-1):
    b +=1/i
print('从左到右计算数列和为：',a)
print('从左到右计算数列和为：',b)


#8.
i = 3
sum = 0
while i <99:
    sum += (i-2)/i
    i +=2
print('和为：',sum)

#9.
pi = 0
for i in range(1,100001):
    pi +=4*((-1)**(1+i)/(2*i-1))
    if i % 10000 ==0:
        print('当i的值为%d时值为：' %i,pi)

#10.**
for i in range(1,10000):
    sum = 0
    for j in range (1,i):
        if i % j ==0:
            sum += j
    if sum == i:
        print(sum,end='\t')

#11.
a = 0
num = int(input('计算到几的组合数：'))
for i in range(1 ,num+1):
    for j in range(1,num+1):
        if i !=j:
            print(i,j)
            a +=1
print('所有可能有：%d种' %a)



