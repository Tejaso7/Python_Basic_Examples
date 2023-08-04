#to print Area of rectangle
class Area:
    def Dia(self):
        self.a = int(input("Enter the length "))
        self.b = int(input("Enter the breadth "))

    def Area(self, a, b):
        area = a*b
        print("Area of Rectangle is:", area)

o = Area()
o.Dia()
o.Area(o.a, o.b)