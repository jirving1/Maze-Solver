from window import *
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    

class Line:
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2
    
    def draw(self, canvas, fill_color):
        canvas.create_line(self.point_1, self.point_2, fill=fill_color, width=2)




