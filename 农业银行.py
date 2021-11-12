print("************************************")
print("*            中国工商银行            *")
print("*            账户管理系统            *")
print("************************************")
print("                                    ")
print("*1.开户                             *")
print("*2.存钱                             *")
print("*3.取钱                             *")
print("*4.转账                             *")
print("*5.查询                             *")
print("*6.Bye                             *")
print("************************************")
dict ={}
import random

def yonghu():
    if len(dict) == 100:
        print("用户库已满")
        return 3
    else:
        return 2

def pass1():
    password1 = input("请输入密码")
    while len(password1) != 6:
        print("请输入6位数密码")
        password1 = input("请输入密码")
    return password1
#添加用户
def yong():
    bank = {}
    yonghu()
    ac = random.randint(100000000, 999999999)
    if ac not in bank:
        print("账户ID:", ac)
        bank[ac] = {}
        name = str(input("输入姓名："))
        bank[ac]["姓名"] = name
        bank[ac]["地址"] = {}
        address1 = input("输入国家:")
        bank[ac]["地址"]["国家"] = address1
        address2 = input("输入省份:")
        bank[ac]["地址"]["省份"] = address2
        address3 = input("输入街道:")
        bank[ac]["地址"]["街道"] = address3
        address4 = input("输入门牌号:")
        bank[ac]["地址"]["门牌号"] = address4
        # password = int(input("输入密码"))
        bank[ac]["密码"] = pass1()
        money = int(input("初始金额"))
        bank[ac]["账户余额"] = money
        bank[ac]["开户行"] = "中国建设银行昌平支行"
        dict.update(bank)
        print(bank)
        print("开户成功！")
        return bank
    return bank
# 存钱
def seve(zhang,jin):
    while True:
        print("进入存钱系统")
        if zhang in dict.keys():
            dict[zhang]["账户余额"] += jin
            print(dict)
            return True
        else:
            print("没有此账户ID")
            return False

# 取钱
def deposit(zhang1,mima,jine):
    while True:
        if zhang1 in dict.keys():
            if dict[zhang1]["密码"] == mima:
                print("密码正确")
                if dict[zhang1]["账户余额"] >= jine:
                    dict[zhang1]["账户余额"] -= jine
                    print(dict)
                    break
                else:
                    print("账户余额不足")
                    return 3
            else:
                print("密码输入错误")
                return 2
        else:
            print("没有此账户ID")
            return 1
#转账
def carry(zhang2,zhang3,mima1,mima2,jine1):
    while True:
        if zhang2 in dict.keys():
            if zhang3 in dict.keys():
                if dict[zhang2]["密码"] == mima1:
                    if dict[zhang3]["密码"] == mima2:
                        if dict[zhang2]["账户余额"] >= jine1:
                            dict[zhang2]["账户余额"] -= jine1
                            dict[zhang3]["账户余额"] += jine1
                            print("转账成功！")
                            print(dict)
                            break
                        else:
                            print("账户余额不足")
                            return 3
                    else:
                        print("密码2错误")
                        return 2
                else:
                    print("密码1错误")
                    return  2
            else:
                print("账户2的ID不存在")
                return 1
        else:
            print("账户1的ID不存在")
            return 1
def query(zhang4,mima3):
    while True:
        if zhang4 in dict.keys():
            if dict[zhang4]["密码"] == mima3:
                print(dict)
                return dict
            else:
                print("密码错误")
                return
        else:
            print("用户不存在")
            return


while True:
    process = input("请选择业务种类")
    if process == "1":
        yong()
    elif process =="2":
        zhang = int(input("输入账户ID"))
        jin = int(input("输入存款金额"))
        seve(zhang,jin)
    elif process =="3":
        zhang1 = int(input("输入账户ID"))
        mima = pass1()
        jine = int(input("输入金额"))
        deposit(zhang1,mima,jine)
    elif process =="4":
        zhang2 = int(input("账号1"))
        zhang3 = int(input("账号2"))
        mima1 = pass1()
        mima2 = pass1()
        jine1 = int(input("输入转出金额"))
        carry(zhang2,zhang3,mima1,mima2,jine1)
    elif process =="5":
        zhang4 = int(input("输入账户ID"))
        mima3 = int(input("密码"))
        query(zhang4,mima3)
    else:
        break