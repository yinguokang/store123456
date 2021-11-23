import time
class Person:
    username = ""
    sex = ""
    aeg = 0
    balance = 0
    brand = ""
    capacity = ""
    screen = 0
    standby = 0
    interral = 0
    def message(self,content):
        print("输入短信内容",content)
    def phone(self,number,time,balance):
        if number == "Null":
            print("号码为空")
        elif balance < 1:
            print("话费余额不足")
        else:
            print("电话拨通")
            print("通话结束，通话时长为",time)
            if time >0 and time <10:
                money = time *1
                balance = balance - money
                print("通话费用为：",money,"话费余额为",balance)
            elif time >=10 and time < 20:
                money = time * 0.8
                balance = balance - money
                print("通话费用为：", money, "话费余额为", balance)
            else:
                money = time * 0.65
                balance = balance - money
                print("通话费用为：", money, "话费余额为", balance)
            return
p = Person()
p.username = "小明"
p.sex = "男"
p.aeg = 25
p.balance = 50
p.brand = "华为"
p.capacity = "1000毫安"
p.screen = 15.6
p.standby = 10
p.interral = 100
p.message("今天上语文课")
p.phone("123456789",30,50)
