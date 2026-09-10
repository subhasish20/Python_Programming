class Test:
    @staticmethod # we use this to declare a static method
    def add( num1:int, num2:int)->int:
        return num1 + num2



obj = Test.add(5,6)
print(obj)
