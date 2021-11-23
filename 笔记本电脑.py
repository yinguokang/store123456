class computer:
    screen = 0
    price = 0
    cpu = ""
    memory = ""
    standby = ""
    def wate(self,watename):
        print(watename)
    def playgame(self,playgamename):
        print("屏幕大小为", self.screen, "的电脑在打", playgamename)
    def film(self,filmname):
        print("屏幕大小为", self.screen, "的电脑在打", filmname)
c = computer()
c.screen = 15.6
c.price = 10000
c.cpu = "GTX"
c.memory = "520G"
c.standby = "12小时"
c.wate("金三打字通")
c.playgame("贪吃蛇")
c.film("海绵宝宝")