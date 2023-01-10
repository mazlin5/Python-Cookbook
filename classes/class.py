# every data structure we create roots from classes
# built in capabliity to create your own data type

class Cookie:
    # constructor
    # method vs function is 'self' - method that's part of a class
    def __init__(self, color):
        self.color = color

    # if only param is self then no arguments passed.
    # returns color for particular color called on
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color

# particular instance of cookie = self
cookie_one = Cookie('green')
cookie_two = Cookie('blue')

print('Cookie one is:', cookie_one.get_color())
print('Cookie two is:', cookie_two.get_color())

cookie_one.set_color('yellow')

print('Cookie one is now:', cookie_one.get_color())
