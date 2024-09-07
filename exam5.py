# a=float(input("Enter the amount in TJS: "))
# rub=a*8.33
# usd=a*0.094
# eur=a*0.084
# us_sum=a*1000
# print(f"""
# Rub-> {rub}
# USD-> {usd}
# EUR-> {eur}
# UZ_SUM-> {us_sum}""")


# 2
# mylist=[int(i) for i in input().split(", ")]
# new=""
# for i in mylist:
#     i=str(i)
#     new+=i
# new=int(new)
# print(new)


# 3
# def salom():
#     a=input()
#     def inner():
#         print("Salom "+a)
#     do=inner()
#     return do
# salom()



# 4
# def minn(a:list,i=0,mini=99999999999999999):
#     if i==len(a):
#         return mini
#     if mini>a[i]:
#         mini=a[i]
#     return minn(a,i+1,mini)
# a=[int(i) for i in input().split()]
# print(minn(a))

# 5
# a=int(input())
# i=1
# sum=0
# while i<=a:
#     sum+=i**2
#     i+=1
# print(sum)


# 6
# def fact(n):
#     s=1
#     for i in range(1,n+1):
#         s*=i
#     return s
# a=int(input())
# i=1
# sum=1
# while i<=a:
#     sum+=1/fact(i)
#     i+=1
# print(sum)


# 7
# a=[i for i in input().split()]
# new=[]
# for j in a:
#     j=str(j)
#     if len(j)>=5:
#         j='#'*len(j)
#         new.append(j)
#     else:
#         new.append(j)
# print(*new)

# 9
# def binar(a,b):
#     if len(a)==1 and b!=a[len(a)//2]:
#         return False
#     if b==a[len(a)//2]:
#         return True
#     elif b>a[len(a)//2]:
#         a=a[len(a)//2:]
#         return binar(a,b)
#     elif b<a[len(a)//2]:
#         a=a[:len(a)//2]
#         return binar(a,b)
# a=[int(i) for i in input().split()]
# b=int(input())
# print(binar(a,b))


# 10
# def scope(a, cnt=0, i=0):
#     if i == 0:  
#         i = len(a) - 1
#     if cnt > i:
#         return ""
#     if cnt == i:
#         return a[cnt]
#     if cnt + 1 == i:
#         return a[cnt:i+1]
#     return a[cnt] + "(" + scope(a, cnt + 1, i - 1) + ")" + a[i]
# a = input()
# print(scope(a))

    
# q1
# Recursiya in : vaqte ki funcsiya dar doxili xudash xudashro faryod mekunad rekursiya meshavad,
#  dar rekursiya funksiya du barobar kor mekunad yane chizhoi kardaashro bolo ba bolo memonad
#  va hangomi koftan yakto yakyo megirad, az in sabab funksiya vaqti ziyodro megirad, 
# qarib dar hama holat az bajoi recursiya loop istifoda karda meshavad



# q2
# closure on vaqt meshavad ki funksiyai dokhili parametr va tagyiryobandahoi az xud berunaro
#  dar yod megirad va bo onho kor karda metavonad 
# misol:
# def exam():
#     a='salom'
#     def inner():
#         return a
#     do = inner()
#     return do
# print(exam())



# q3
# konteynerho: list,tuple,dict,set
# konteynerho yakchand elemntro dar dokhilashon girifta metavonand yane collection 
# list bo [] navishta meshavad va dilxoh tip danniro qabul mekunad va dar on CRUD kor mekunad
# dict {} formati key:value dorad yaane indexosh nom dorand
# tuple () misli list ast vale dar on crud purra kor namekunad 
# set {} collecsiyaest ki unordered hast va xudash mutable elementhoyaash immutable meboshad mo elementhoi onro update karda nametavonem chunki order nadorand

# q4
# coomprehensions 
# yane mo ba list va dict usloviyaro hangomi doxil kardanash medihem
# misol: int(i) for i in input().split() if i%2==0
# dar injo faqat elementhoi juft qabul meshavan az bayni dokhil kardahoi user
# args va kvargs boshad bo du sitora pesh az nomashon dar function navishta meshavand ki tarzi qabuli elementhoyand va args elementhor 
# ki znacheniye nadorand qabul meshavad va kvargs boshad monandi formati key:value dar xotir megirad yane hangomi navishtani a=50 onro chun 'a':50 megirad va arg boshad oddi xudi hamon elementro

# q5
# datetime dorad datetime,time,timedelta,date 
# metodhoi on :
# today-imruzro muayyan mekunad
# time-vaqtro meguyad
# date-ruzro
# replace-ta`rixi ruzi navro vorid mekunem
#`strptime-az string datetimro megiraf yane ruz moh sol ,....
# strftime-in muayyan mekunad az chizi dodashuda lozimaro: misol agar formati %d-ruzro %m-raqami mohro, %H-soatro va gayra 


# random daraad random-az 0.0 to 1.0 yagon adad megirad
# randint(a,b) az a to b yagon adadi butun megirad
# randrange in boz stepham dorad misol vaqte az bayni dau adad yakto girift adadi oyandaash ba step ziyod ast
# misol agar az bayni (1,10,3) 4-ro girift bad 7ro megirad
# random.choice az listi dodashuda yak elemenro megirad
# rand0m.choices chand elementi lozim boshad medihem shumoraashro onhoro megirad va boz weight dorad ki mo shansi yagon elemntro bisyortar mekunem
# sample misli choices ast vale weight nadorad
