from window import Point, Line, Window, Cell


def main():
    win = Window(800, 600)
    cell = Cell()
    cell.draw(100, 150, 200, 250, win)
    win.wait_for_close()
    
main()