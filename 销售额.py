import xlrd
f = xlrd.open_workbook(filename=r"D:\python\pythonxiangmushuju\day08\2020年每个月的销售情况.xlsx",encoding_override=True)


#销售总额
sums = []
def zhong():
    j=0
    while j<12:
        sheet = f.sheet_by_index(j)
        j=j+1
        rows = sheet.nrows
        cols = sheet.ncols
        sum_dan = 0
        sum_zhong = 0
        q=0
        for i in range(1,rows):
            data = sheet.row_values(i)
            sum_dan = data[2] * data[4]
            sum_zhong = sum_zhong + sum_dan
        sums.append(sum_zhong)
        sum1 = sum(sums)
    print("总销售额为:",sum1)
    return
zhong()




#每种衣服的销售占比
dict = {}
def new():

    list = []
    while True:
        shu = 0
        usname = input("输入商品名")
        if usname != "q":
            j = 0
            while j<12:
                sheet = f.sheet_by_index(j)
                j = j + 1
                rows = sheet.nrows
                cols = sheet.ncols
                for i in range(1,rows):
                    data1 = sheet.row_values(i)
                    if data1[1] == usname:
                        shu= shu + data1[4]
                        dict.update({usname:shu})
            print(dict)
        else:
            break

    return dict
new()
jian = 0
print("羽绒服的占比:{:.0%}".format(dict["羽绒服"]/jian))
print("牛仔裤的占比:{:.0%}".format(dict["牛仔裤"]/jian))
print("风衣的占比:{:.0%}".format(dict["风衣"]/jian))
print("皮草的占比:{:.0%}".format(dict["皮草"]/jian))
print("T恤的占比:{:.0%}".format(dict["T恤"]/jian))
print("马甲的占比:{:.0%}".format(dict["马甲"]/jian))



j = 0
he = 0
sum_yu=0
sum_niu = 0
sum_feng = 0
sum_pi = 0
sum_ma = 0
sum_t = 0
sum_xiao = 0
dict1 = {}
while j<12:
    sheet = f.sheet_by_index(j)
    j=j+1
    rows = sheet.nrows
    cols = sheet.ncols
    for i in range(1, rows):
        data1 = sheet.row_values(i)
        # print(data1)
        he = he + data1[4]
        if data1[1] == "羽绒服":
            sum_yu = sum_yu + data1[4]
        elif data1[1] == "牛仔裤":
            sum_niu = sum_niu + data1[4]
        elif data1[1] == "风衣":
            sum_feng = sum_feng + data1[4]
        elif data1[1] == "皮草":
            sum_pi = sum_pi + data1[4]
        elif data1[1] == "马甲":
            sum_ma = sum_ma + data1[4]
        elif data1[1] == "T血":
            sum_t = sum_t + data1[4]
        elif data1[1] == "小西装":
            sum_xiao = sum_xiao + data1[4]
    print(j,"月羽绒服的占比:{:.0%}".format(sum_yu/he))
    print(j,"月牛仔裤的占比:{:.0%}".format(sum_niu/he))
    print(j,"月风衣的占比:{:.0%}".format(sum_feng/he))
    print(j,"月皮草的占比:{:.0%}".format(sum_pi/he))
    print(j,"月马甲的占比:{:.0%}".format(sum_ma/he))
    print(j,"月T恤的占比:{:.0%}".format(sum_t/he))
    print(j,"月小西装的占比:{:.0%}".format(sum_xiao/he))







