
# Any object containing execute(self) method is considered to be IDE App
# this is Duck typing concept

class PyCharm:
    def execute(self):
        print("pycharm ide runnig")

class MyIde:
    def execute(self):
        print("MyIde running")

class Laptop:

    def code(self,ide):
        ide.execute()

ide=MyIde()

obj=Laptop()

obj.code(ide)
