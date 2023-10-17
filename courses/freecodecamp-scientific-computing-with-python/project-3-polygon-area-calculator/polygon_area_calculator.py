def main():
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())

    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
        
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height  ** 2) ** .5

    def get_picture(self):
        picture = ""
        if self.width > 50 or self.height > 50:
            return f"Too big for picture."
        else:
            for column in range(self.height):
                for row in range(self.width):
                    picture += "*"
                picture += "\n"
            return picture

    def get_amount_inside(self, object):
        return (self.width // object.width) * (self.height // object.height)


class Square(Rectangle):
    def __init__(self, side):
        Rectangle.__init__(self, side, side)

    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self,side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.height = height
        self.width = height

    def get_perimeter(self):
        return super().get_perimeter()
    
    def get_diagonal(self):
        return super().get_diagonal()

    def get_picture(self):
        return super().get_picture()
    
    def get_amount_inside(self, object):
        return super().get_amount_inside(object)


if __name__ == "__main__":
    main()