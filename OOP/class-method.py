
class Demo:
    name = "subhasish jena"

    def __init__(self) -> None:
        print(Demo.name)

    @classmethod # by declaring classmethod we can modify the data inside the class
    def change_name(cls,new_name):
        cls.name = new_name



obj =  Demo()

Demo.change_name("Name changed")

obj = Demo()
