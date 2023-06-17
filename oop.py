class Rectangle :
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def parimeter(self):
        return ( self.length + self.width) * 2
    def area(self):
        return (self.length *  self.width)
    def display(self):
        print('Length',self.length)
        print('Width', self.width)
        print(self.parimeter())
        print(self.area())
shape = Rectangle(3,6)
parimeter =shape.parimeter()
area = shape.area()
print( 'The parimeter = ',parimeter, 'The area = ' ,area)
shape.display()

class Parallelepipede(Rectangle):
     def __init__(self, length, width,height):
        self.height = height
        Rectangle.__init__(self,length,width)
     def volume (self):
        return (self.height * self.length * self.width)
volume1 = Parallelepipede(3,7,8)
volume = volume1.volume()
print(volume)


