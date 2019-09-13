#1.读取成绩并输出成绩等级
def scores(a,b,c,d):
   x = [a,b,c,d]
   y = sorted(x)
   z = y[3]
   for i in range(len(x)):
       if x[i] >= z - 10:
           print('成绩为A')
       elif x[i] >= z - 20:
           print('成绩为B')
       elif x[i] >= z - 30:
           print('成绩为C')
       elif x[i] >= z - 40:
           print('成绩为D')
       else:
           print('成绩为F')
scores(40,55,70,58)


##2.逆序顺序显示一个整数列表：
a = [1,2,3,4,0,9,8,7]
b = a[::-1]
print(b)



#6.返回最小元素的下标
def indexOFSmallestElement(A1):
   A1 = lst
   A2 = sorted(A1)
   min_ = A2[0]

   for i in range(len(A1)):
       if A1[i] == min_:
           print('最小元素的下标>>%d'%(i+1))
           
indexOFSmallestElement([3,4,2,7,5,4,1,4,3,4])



# 4.输入字符串显示字母数
def countletters(s):
    zi=[]
    for i in s:
        b=0
        for a  in s:               
            if  a == i:
                b+=1
                zm=str(a)+'出现了'+str(b)+'次'
        zi.append(zm)
        zi_=set(zi)
        zi__=sorted(list(zi_))
    for i_ in zi__:
        print(i_)
countletters('icosnvowvinwbeuiboivn') 







 