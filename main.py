
import csv
import tkinter as tk


class Programconfig:
    def __init__(self, configfile):
        # A List of words
        self.cfgdata = []
        self.cfgfile = configfile
    def readconfig(self):
        try:
            with open(self.cfgfile, "r") as filehandle:
                for line in csv.reader(filehandle):
                    print(line)
        except:
            print("Error on open file for read")


class App(tk.Tk):
    def __init__(self,Title,Geometry):
        super().__init__()
        self.title(Title)
        self.geometry(Geometry)
        self.label = tk.Label(self, text="Hello")
        self.label.pack()
        self.button = tk.Button(self, text='Click Me')
        self.button['command'] = self.button_clicked
        self.button.pack()

    def button_clicked(self):
        T = tk.Text(self, height=500, width=200)
        T.pack()
        self.label.pack()






if __name__ == '__main__':
    print("Program Config")
    cfg = Programconfig("config.csv")
    cfg.readconfig()

    app = App('myTitle','300x50')
    app.mainloop()

