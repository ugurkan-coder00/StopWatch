from tkinter import *

class stopwatch:
    def __init__(self,title = "StopWatch",geometry = "400x75") -> None:
        self.title = title
        self.geometry = geometry
        self.color = "black"
        self.text_color = "gold"

    def Screen(self):
        self.root = Tk()
        self.root.title(self.title)
        self.root.geometry(self.geometry)
        self.root.configure(bg = self.color)
        self.root.resizable(0,0)
        self.root.iconphoto(False,PhotoImage(file = "icon.png"))

    def clock(self):
        def tool():
            if self.start == True:
                self.time[2] += 1
                if self.time[2] >= 100:
                    self.time[2] = 0
                    self.time[1] += 1
                if self.time[1] >= 60:
                    self.time[1] = 0
                    self.time[0] += 1
                formatt = self.word.format(self.time[0],self.time[1],self.time[2])
                self.l.configure(text = formatt)
            self.root.after(9,tool)
        self.time = [0,0,0]
        self.word = "{0:02d}:{1:02d}:{2:02d}"
        self.start = False
        self.l = Label(self.root,text = "00:00:00",bg = self.color,fg = self.text_color,font=("Arial",50,"bold"))
        self.l.pack()
        self.l.place(x = 0,y = 0)
        tool()
    # BUTTON COMMANDS
    def play_command(self):
        self.start = True
        print("PLAY")

    def pause_command(self):
        self.start = False
        print("PAUSE")

    def reset_command(self):
        self.start = False
        self.time[0] = 0
        self.time[1] = 0
        self.time[2] = 0
        self.start = True
        print("RESET")

    def exit_command(self):
        self.start = False
        self.root.quit()

    def buttons(self):
        self.play = Button(self.root,bg = self.color,fg = "blue",text = "PLAY",highlightthickness=0,borderwidth=0,font=("Arial",12,"bold"),command=self.play_command)
        self.play.pack()
        self.play.place(x = 275,y = 0,width=60)

        self.pause = Button(self.root,bg = self.color,fg = "yellow",text = "PAUSE",highlightthickness=0,borderwidth=0,font=("Arial",12,"bold"),command=self.pause_command)
        self.pause.pack()
        self.pause.place(x = 335,y = 0,width=60)

        self.reset = Button(self.root,bg = self.color,fg = "white",text = "RESET",highlightthickness=0,borderwidth=0,font=("Arial",12,"bold"),command=self.reset_command)
        self.reset.pack()
        self.reset.place(x = 275,y = 40,width=60)

        self.exit = Button(self.root,bg = self.color,fg = "red",text = "EXİT",highlightthickness=0,borderwidth=0,font=("Arial",12,"bold"),command=self.exit_command)
        self.exit.pack()
        self.exit.place(x = 335,y = 40,width=60)

    def loop(self):
        self.root.mainloop()

a = stopwatch()
a.Screen()
a.clock()
a.buttons()
a.loop()
