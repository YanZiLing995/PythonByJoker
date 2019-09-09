#1.
f=(9 / 5)* c + 32
c = float(input('请输入摄氏温度'))
f =(9 / 5) * c + 32
print('%0.1f摄氏度是%0.1f华氏度' %(c,f))

#2.
#area = r * r *Π
#volume = area *length
import math
r = float(input('请输入圆柱的半径'))
l = float(input('请输入圆柱的高'))
area = r * r *math.pi
volume = area * l
print('圆柱的底面积为%0.4f' %area)
print('圆柱的体积为%0.1f' %volume)

#3.
#一英尺等于0.305米
ft = float(input('请输入英尺的值'))
metre = 0.305 * ft
print('%0.1f英尺等于%0.4f米' %(ft,metre))

#4.
Q = M * (finalTemp-initialTemp) * 4184
M = float(input('请输入以千克计算的水量：'))
initialTemp = float(input('请输入初始温度：'))
finalTemp = float(input('请输入最终温度：'))
Q = M * (finalTemp-initialTemp) * 4184
print('能量为%0.1f' %Q)

#5.
#利息 = 差额 *（年利率 /1200）
chae = int(input('请输入差额'))
nll = float(input('请输入年利率'))
lixi = chae * (nll / 1200)
print ('下个月的月供利息为%0.5f' %lixi)

#6.
#a = (v1 - v0 )/ t 
v0 = float(input('请输入初始速度'))
v1 = float(input('请输入末速度'))
t = float(input('请输入以秒为单位的时间'))
a = (v1 - v0 )/t 
print('平均加速度为：%0.5f' %a)

#7.
# 第一个月：100 *（1 + 0.00417） = 100.417
# 第二个月：（100 + 100.417） * （1 + 0.00417）=201.252
# 第三个月：（100 + 201.252） * （1 + 0.00417）=302.507

month = int(input('请输入每月的存款'))
sum = 0
for i in range(6):
    sum = (month + sum ) * (1 + 0.00417)
print('6个月后的金额为：%0.3f' %sum)

#8.
num = int(input('请输入一个0-1000之间的数：'))
sum =(num % 10)+((num//10) % 10) + (num//100)
print('和为：%d' %sum)






