from Tkinter import *
from PIL import ImageGrab, ImageTk
from PIL import Image
from PIL import ImageDraw
import compare
class Paint(object):

    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'

    # Constructor for Paint window
    def __init__(self):
        self.root = Tk()
        self.root.title("Sketch Search")
        self.image1 = Image.new("RGB", (256, 256), (255,255,255))
        self.draw = ImageDraw.Draw(self.image1)
        self.pen_button = Button(self.root, text='Pen',command=self.use_pen)
        self.pen_button.grid(row=0, column=0)

        self.reset_button = Button(self.root, text='Reset', command=self.reset)
        self.reset_button.grid(row=0, column=2)

        self.process_button = Button(self.root, text='Process', command=self.process)
        self.process_button.grid(row=0, column=3)

        self.eraser_button = Button(self.root, text='Eraser', command=self.use_eraser)
        self.eraser_button.grid(row=0, column=1)

        self.choose_size_button = Scale(self.root, from_=1, to=10, orient=HORIZONTAL)
        self.choose_size_button.grid(row=0, column=4)

        self.suggest = Label(self.root)


        self.c = Canvas(self.root, bg='white', width=256, height=256)
        self.c.grid(row=1, columnspan=5)

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.pen_button
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def use_pen(self):
        self.activate_button(self.pen_button)

    def reset(self):
        self.c.delete('all')

    def process(self):
        self.eraser_on = False
        # self.color = askcolor(color=self.color)[1]
        filename = "my_drawing.jpg"
        self.image1.save(filename)
        num=compare.fetch()
        print num
        img = ImageTk.PhotoImage(Image.open('sample_images/'+str(num)+'.png'))
        self.suggest.image=img
        self.suggest.configure(image=img)
        self.suggest.grid(row=0, column=5, columnspan=5)


    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True)



    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        paint_color = 'white' if self.eraser_on else self.color
        self.line_width= 15 if self.eraser_on else self.choose_size_button.get()
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)

            self.draw.line([self.old_x, self.old_y, event.x, event.y],fill=paint_color,width=self.line_width)

        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None

ge = Paint()