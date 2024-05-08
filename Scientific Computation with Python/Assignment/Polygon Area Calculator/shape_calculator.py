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
        area = self.width*self.height
        return area
    
    def get_perimeter(self):
        return 2*(self.height + self.width)
    
    def get_diagonal(self):
        return (self.height**2 + self.width**2)**0.5 # teorema di pitagora
    
    def get_picture(self):
        '''
        Return a picture made of "*" 
        '''
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        
        pic = '*' * self.width + '\n'
        pic = pic * self.height
        return pic
    
    def get_amount_inside(self, figure):
        '''
        Takes another shape (square or rectangle) as an argument. 
        Returns the number of times the passed in shape could fit inside the shape (with no rotations). 
        For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with 
        sides of 4.
        '''
        return self.get_area() // figure.get_area()


class Square(Rectangle):
    '''
    Should be a subclass of Square
    '''
    def __init__(self, width):
        self.width = width
        self.height = width
        
    def __str__(self):
        return f"Square(side={self.width})"
    
    def set_side(self, side):
        self.width = side
        self.height = side

