# 1
# mylist=[1,1,2,3,4,4,5,1]
# a=int(input())
# mylist.insert(3,"Sorbon")
# print(mylist)


# 2
# from datetime import datetime,timedelta
# res=datetime.today().date()
# res1=res+timedelta(-2)
# res2=res+timedelta(2)
# print("pareruz:",res1)
# print("imruz:",res)
# print("fardo:",res2)


# 3
# from datetime import datetime,timedelta
# a=input().split('.')
# day,month,year=map(int,a)
# res=datetime(year,month,day)
# new=res+timedelta(-5)
# new2=datetime.strftime(new, "%d.%m.%Y")
# print(new2)


# 4
# def vowels(a):
#     sum=0
#     for i in a:
#         i=str(i)
#         for j in i.lower():
#             if j=='a':
#                 sum+=4
#             elif j=='e':
#                 sum+=3
#             elif j=='i':
#                 sum+=1
#     print(sum)
# a=input().split()
# vowels(a)


# 5
# with open("exam.txt", 'r') as file:
#     res = file.readlines()
#     a=int(input())-1
#     for i in range(len(res)):
#         print(res[a])
#         break


# 6
# with open("exam.txt",'r') as file:
#     res=file.readlines()
#     a=input("kalimaatonro doxil kuned: ")
#     for i in range(len(res)):
#         if i%2==0:
#             res[i]=a
#     for i in res:
#         print(i.strip())
            

# 7
# import random
# a=int(input())
# b="qwertyuiopasdfghjklzxcvbnm1234567890!@#$%&*QWERTYUIOPASDFGHJKLZXCVBNM"
# new=random.choices(b, k=a)
# m=""
# for i in new:
#     m+=i
# print(m)    


# 8
# a=int(input())
# mydict={}
# for i in range(1,a+1):
#     mydict[i]=i**2
# print(mydict)



# 9
# def counter(x):
#     a=str(x[0]).split()
#     m=str(x[1])
#     mylist=[]
#     for i in a:
#         i=str(i).lower()
#         cnt=0
#         for j in i:
#             if j==m:
#                 cnt+=1
#         mylist.append(cnt)
#     print(mylist)
# x=input().split(',')
# counter(x)


# 10
# mylist=[i for i in input().split()]
# new={
#     "int":[],
#     "str":[],
#     "bool":[]
# }
# for i in mylist:
#     if i.isdigit():
#         new["int"].append(int(i))
#     elif i.isalpha() and i!='True' and i!='False':
#         new["str"].append(i)
#     elif i=="True" or i=="False":
#         if i=="True":
#             new["bool"].append(True)
#         else:
#             new["bool"].append(False)
# print(new)




# Q1
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



# Q2
# baroi kor bo fail mo dorem open ki mekushoyad yagon failro vale mode dorad ki mo no fail chikor mekunem misoli 'r'-baroi xondan, 'w'-navistan boz agar fail naboshad onro mesozad va chandtoi digar
# dore close baroi maxkam kardani fail badi kor
# in korro avtomati with open mekunad
# baroi kor bo xudi fail dorem readlines() ki har satri failro mexonadu ba yak listi nav megardonad
# write baroi dar file yagonchizi nav navishtan


# Q3
# github yak platformaest ki dar on razrabotchikho kodhoi xudro metavonand ki yakjoya kunand
# dorem git init repositorii nav mekushoyad
# add dobavit mekunad
# rm udalit mekunad
# commit tagyirothoro ilova mekunad
# status mebinad ki dar repositorii mo chi hast
