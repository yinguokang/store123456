#每个人的平均工资
#     姓名  年龄  性别  编号   任职公司   薪资   部门编号
from numpy import *
names = [
    ["曹操","56","男","106","IBM", 500 ,"50"],
    ["大乔","19","女","230","微软", 501 ,"60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["许褚", "45", "男", "230", "Tencent", 700 , "10"]
]
names1=[i[5] for i in names]
print(names1)
q=0
for j in range(0, len(names1)):
    q=q + names1[j]
print("总工资为：",q)
print("平均工资为：",mean(names1))
names.append(["刘备","45","男","220","alibaba", 500 ,"30"])#添加新员工
print(names)
#男女人数
names2=[e[2] for e in names]
print(names2)
t=0
d=0
for w in names2:
    if w=='男':
        t=t+1
    elif w=="女":
        d=d+1
print("女生人数:",d)
print("男生人数为：",t)
#平均年龄
names1=[i[1] for i in names]
print(names1)
kong = [];
for n in names1:
    kong.append(int(n));
names1 = kong;
print(kong)
# names1=[int(x) for x in names1 ]
# print(names1)
j=0
for i in range(0,len(kong)):
    print(kong[i])
    j=j+kong[i]
print("员工的平均年龄为：",mean(kong))
#每个部门的人数
names1=[i[6] for i in names]
print(names1)
print("部门编号50有",names1.count('50'),"人")
print("部门编号60有",names1.count('60'),"人")
print("部门编号10有",names1.count('10'),"人")
print("部门编号30有",names1.count('30'),"人")

