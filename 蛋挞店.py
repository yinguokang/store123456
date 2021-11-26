from  threading import Thread

import time
wight=0 #全局变量 蛋挞池子

class cooker(Thread): #定义一个厨师类
    cooker_name=""
    wight_sum=0
    def run(self)->None:
        global wight
        start=time.time()
        while True:
            end=time.time()
            if end - start<60 :
                if wight <500:
                    self.wight_sum=self.wight_sum+1
                    eggpool=wight +1
                else:
                    time.sleep(3)
            else:
                break
        return self.wight_sum


class customer(Thread):#定义一个顾客类
    customer_name=""
    money=5000.0
    many=0
    def run(self)->None:
        global  wight
        start=time.time() #开始时间
        while True:
            end=time.time() #结束时间
            if end - start<60:   #时间60秒
                if wight > 0:

                    if self.money >= 3:
                        self.money = self.money - 3
                        wight = wight - 1
                        self.many = self.many + 1
                    else:
                        break
                else:
                    time.sleep(2)
            else:
                break

        return self.many


c1=cooker()
c2=cooker()
c3=cooker()
cu1=customer()
cu2=customer()
cu3=customer()
cu4=customer()
cu5=customer()
cu6=customer()
c1.cooker_name="厨师1"
c2.cooker_name="厨师2"
c3.cooker_name="厨师3"
cu1.customer_name="顾客1"
cu2.customer_name="顾客2"
cu3.customer_name="顾客3"
cu4.customer_name="顾客4"
cu5.customer_name="顾客5"
cu6.customer_name="顾客6"

c1.start()
c2.start()
c3.start()
cu1.start()
cu2.start()
cu3.start()
cu4.start()
cu5.start()
cu6.start()


c1.join()
c2.join()
c3.join()
cu1.join()
cu2.join()
cu3.join()
cu4.join()
cu5.join()
cu6.join()



print(c1.cooker_name, "做出了", c1.wight_sum, "个蛋挞!","工资",c1.wight_sum*1.5)
print(c2.cooker_name, "做出了", c2.wight_sum, "个蛋挞!","工资",c2.wight_sum*1.5)
print(c3.cooker_name, "做出了", c3.wight_sum, "个蛋挞!","工资",c3.wight_sum*1.5)
print(cu1.customer_name,"一共抢了",cu1.many,"个蛋挞")
print(cu2.customer_name,"一共抢了",cu2.many,"个蛋挞")
print(cu3.customer_name,"一共抢了",cu3.many,"个蛋挞")
print(cu4.customer_name,"一共抢了",cu4.many,"个蛋挞")
print(cu5.customer_name,"一共抢了",cu5.many,"个蛋挞")
print(cu6.customer_name,"一共抢了",cu6.many,"个蛋挞")
