from tkinter import Tk, BOTH, Canvas
from lines import *

class Window:
    def __init__(self, width, height): #width and height are in pixels
       self.root_widget = Tk()
       self.canvas = Canvas()
       self.canvas.pack(fill = BOTH, expand = True)
       self.is_window_open = False
       self.root_widget.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.root_widget.update_idletasks()
        self.root_widget.update()

    def wait_for_close(self):
        self.is_window_open = True
        while self.is_window_open == True:
            self.redraw()
    
    def close(self):
        self.is_window_open = False

    def draw_line(self, Line, fill_color="Black"):
        Line.draw(self.canvas, fill_color)

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    

class Line:
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2
    
    def draw(self, canvas, fill_color):
        canvas.create_line(self.point_1.x, self.point_1.y, self.point_2.x, self.point_2.y, fill=fill_color, width=2)


class Cell:
    def __init__(self, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall

    def draw(self, _x1, _y1, _x2, _y2, _win):
    # x1, y1 are top left; x2, y2 are bottom right
        if self.has_left_wall:
            _win.draw_line(Line(Point(_x1, _y1), Point(_x1, _y2)))  # Vertical left wall
        if self.has_right_wall:
            _win.draw_line(Line(Point(_x2, _y1), Point(_x2, _y2)))  # Vertical right wall
        if self.has_top_wall:
            _win.draw_line(Line(Point(_x1, _y1), Point(_x2, _y1)))  # Horizontal top wall
        if self.has_bottom_wall:
            _win.draw_line(Line(Point(_x1, _y2), Point(_x2, _y2)))  # Horizontal bottom wall





        