sums=[
    ["罗恩", 23 ,35 ,44]
    ,["哈利" ,60, 77 ,68 ,88, 90]
    ,["赫敏", 97 ,99 ,89 ,91, 95, 90]
    ,["马尔福" ,100, 85 ,90]
]
b=sums[0]
j=0
for i in range(1,len(b)):
    j=j+b[i]
print("罗恩的总成绩：",j)
h=sums[1]
q=0
for e in range(1,len(h)):
    q=q+h[e]
print("哈利的总成绩：",q)
b=sums[2]
j=0
for i in range(1,len(b)):
    j=j+b[i]
print("赫敏的总成绩：",j)
b=sums[3]
j=0
for i in range(1,len(b)):
    j=j+b[i]
print("马尔福的总成绩：",j)