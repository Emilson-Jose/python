import tkinter as gui

m = gui.Tk()
m.title('App Window')

button = gui.Button(m, text='Stop', width=15, command=m.destroy, activeforeground='red')
button.pack()

w = gui.Canvas(m, width=40, height=60)
w.pack()
canvas_h = 50
canvas_w = 2000
y = int(canvas_h / 2)
w.create_line(0, y, canvas_w, y)

var1 = gui.IntVar()
b1 = gui.Checkbutton(m, text='male', variable=var1)  #.grid(row=0, sticky='w')
var2 = gui.IntVar()
b2 = gui.Checkbutton(m, text='female', variable=var2)  #.grid(row=1, sticky='w')
b1.pack()
b2.pack()

m.mainloop()

#def main():
#    print("hello")

#if __name__ == "__main__":
#    main()