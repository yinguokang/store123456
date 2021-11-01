
# list=["北京","上海","广东"]
# print(list)
# list.append("济南")
# list.append("郑州")
# print(list)

# def num(list,num1,num2):
#     list[num1], list[num2] = list[num2], list[num1]
#     return list
# list = ["北京","上海","广东","济南","郑州"]
# num1,num2=1,4
# print(num(list,num1-1,num2-1))

i = 0

list=[36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
for sum1 in range(0, len(list)):
    i = i + list[sum1]
print("GDP之和为: ", i)
j=i/8
print("平均GDP为：",j)


