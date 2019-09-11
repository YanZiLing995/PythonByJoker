#1.
# n = 1
# def getPentagonalNumber (n):    
#     for n in range(1,101):
#         m = n*(3*n - 1)/2
#         print('%d' %m,end='\t') 
#         if n % 10 ==0:
#             print('\n') 
         
# getPentagonalNumber(n)    

#2.*

# def sumDigits(n):
#     sum = 0
#     for i in range(len(str(n))):
#         num = n//10**i %10
#         sum += num    
#     print('和为：%d' %sum)
# def test():
#     n = int(input('输入一个整数:'))
#     sumDigits(n)
# test()

#3.
# def displaySortedNumber(num1,num2,num3):
#     list=[num1,num2,num3]
#     list.sort()
#     print('升序为：')
#     for i in range(len(list)):
#         print(list[i])

# def num():
#     num1,num2,num3 = eval(input('请输入三个整数:'))
#     displaySortedNumber(num1,num2,num3)  
# num()

#.4
# def num(x,y):
#     for i in range(1,31):
#         s = float(x * ((1 + y) ** i))
#         print('%.2f'%s)
    
# num(1000,0.09)

#.5
# count = 0
# def pri(ch1,ch2):
#     global count
#     x = ord(ch1)
#     y = ord(ch2)
#     for i in range(x,y + 1):
#         print(chr(i),end="")
#         count += 1
#         if count % 10 == 0:
#             print("\t")
# pri('1','z')

#.6
# def year(y1,y2):
#     for i in range(y1,y2+1):
#         if i % 4 == 0 and i % 100 != 0 or i % 400 ==0:
#             print('%d年有366天'%i)
#         else:
#             print('%d年有365天'%i)
# year(2010,2020)
#.7
# import math
# def dis(x1,y1,x2,y2):
#     h = float(math.sqrt((x1 - x2) ** 2 + (y1 - y1) ** 2))
#     print(h)
# dis(6,3,2,4)
#.8
# a=[]
# for i in range(1,100):
#     for j in range(2,i):
#         if (i % j == 0):
#             break
#     else:
#         a.append(i)

#.9
# def time_():
#     import time
#     t = time.localtime(time.time())
#     format_time='%a  %Y-%m-%d  %H:%M:%S'
#     cur_time = time.strftime(format_time,t)
#     print (cur_time)
# time_()

#.10
# import random

# a = random.randint(1,6)
# b = random.randint(1,6)
# c = a + b
# if c == 2 or c == 3 or c == 12:
#     print('you rolled %d+%d=%d:'%(a,b,c))
#     print('you lose')
# elif c == 7 or c == 11:
#     print('you rolled %d+%d=%d:'%(a,b,c))
#     print('you win')
# else:
   
#     print('you rolled %d+%d=%d:'%(a,b,c))
#     print('point is %d'%c)
#     x = random.randint(1,6)
#     y = random.randint(1,6)
#     s = x + y
#     print('you rolled %d+%d=%d:'%(x,y,s))
#     if c == s:
#         print('you win')
#     else:
#         print('you lose')

 









