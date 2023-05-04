class Circle:
    def __init__(self , radius):
        self.radius = radius
    def area(self):
        return 3.14 * (self.radius ** 2)
name = Circle(32)
print("Радіус:" , name.radius)
print("Площа:" , name.area())
