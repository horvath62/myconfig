
import csv
import tkinter as tk


class Programconfig:
    def __init__(self, configfile):
        # A List of words
        self.cfgdata = {}
        self.cfgfile = configfile
        self.cfgerror = []
    def readconfig(self):
        try:
            with open(self.cfgfile, "r") as filehandle:
                for line in csv.reader(filehandle):
                    print(line)
                    if len(line) > 1:
                        self.cfgdata[line[0]] = line[1]
                    else:
                        self.cfgerror.append(line[0])
        except IOError:
            print("Error opening file")
        except:
            print("Error in config file")

    def printconfig(self):
        print(self.cfgdata)
        if len(self.cfgerror) > 0:
            print("Error in config file:")
            print(self.cfgerror)


class App(tk.Tk):
    def __init__(self,Title,Geometry):
        super().__init__()
        self.title(Title)
        self.geometry(Geometry)
        self.label1 = tk.Label(self, text="Hello")
        self.label2 = tk.Label(self, text="Parameter")
        self.label1.grid(row = 0, column = 0, pady = 2)
        self.label2.grid(row=0, column=1, pady=2)
        self.button1 = tk.Button(self, text='Click Me')
        self.button1['command'] = self.button1_clicked
        self.button1.grid(row = 3, column = 1)
        self.button2 = tk.Button(self, text='Click Me')
        self.button2['command'] = self.button2_clicked
        self.button2.grid(row = 3, column = 2)
        self.text1 = tk.Text(self, height=2, width=20)
        self.text1.grid(row=2,column = 1)
        self.text1.insert(tk.END,"some text")
        self.text2 = tk.Text(self, height=2, width=20)
        self.text2.grid(row=2, column=2)
        self.text2.insert(tk.END, "more text")

        self.check1 = tk.Checkbutton(self)
        self.check1.grid(row=1, column=0)
        self.check2 = tk.Checkbutton(self)
        self.check2.grid(row=2, column=0)


    def button1_clicked(self):
        # T = tk.Text(self, height=2, width=20)
        self.text1.insert(tk.END, "longer.........text")

    def button2_clicked(self):
        # T = tk.Text(self, height=2, width=20)
        self.text2.insert(tk.END, "longer.........text")


if __name__ == '__main__':
    print("Program Config")
    cfg = Programconfig("config.csv")
    cfg.readconfig()
    cfg.printconfig()

    app = App('myTitle','500x500')
    app.mainloop()

