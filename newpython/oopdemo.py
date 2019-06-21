class Camera:
    def __init__(self, mo="加特林"):
        self.model = mo
    def snapshot(self):
        print("照相机%s拍了一张照片"%self.model)

class Phone(Camera):
    def call(self):
        print("手机%s正在通话"%self.name)
    def snapshot(self):
        print("手机%s截图保存了屏幕"%self.name)

class GameBox(Phone,Camera):
    def play(self):
        print("游戏机%s正在运行游戏"%self.name)
    def snapshot(self):
        print("游戏机%s截图保存了屏幕"%self.name)

def powerOn(ojc,):
    print("启动")

x = GameBox()
x.name = "Xbox"
x.powerOn = powerOn()
x.powerOn(x,)
x.play()
x.call()
x.snapshot()
print(GameBox.mro())
