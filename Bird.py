class Bird:
    def __init__(self, attribute,color):
        self.name=attribute
        self.color=color

    def color(self):
        print(f"My color is{self.color}")

    def type(self):
        print(f"What type of bird is this{self.name}")
if __name__ == '__main__':
    a=input("What is the name of bird 1?")
    b=input("What is the name of bird 2?")
    x = Bird(a, "yellow")
    print(x.name)
    print(x.color)
    y=Bird(b,"green")
    print(y.name)
    print(y.color)
