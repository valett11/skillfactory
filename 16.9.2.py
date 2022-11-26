class Rectangle:
    def __init__(self, x,y, width,heigth):
        self.x = x
        self.y = y
        self.width=width
        self.heigth=heigth
    def __str__(self):
        return f"Rectangle: {self.x},{self.y},{self.width}, {self.heigth}"

r1 =  Rectangle(1,1,10,11)
print(r1)