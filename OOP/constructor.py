
class Animal:
    def __init__(self,name:str, type:str, color:str) -> None:
        self.name = name
        self.type = type
        self.color = color



def main():
    obj = Animal("Tiger","domestic","black")

    print("The name of the animal is ",obj.name)
    print(f"The type of the {obj.name} is {obj.type}")
    print(f"The color of {obj.name} is {obj.color}")

if __name__ == "__main__":
    main()
