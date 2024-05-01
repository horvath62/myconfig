
import csv
import tkinter as tk


class Programconfig:
    def __init__(self, configfile):
        # A List of words
        self.cfgdata = {}
        self.cfgfile = configfile
        self.cfgignore = []
        print("Program Config")
    def readconfig(self):
        try:
            with open(self.cfgfile, "r") as filehandle:
                for line in csv.reader(filehandle):
                    # print(line)
                    # print(len(line))
                    if len(line) > 1:
                        if line[0][0] == "#":
                            self.cfgignore.append(' '.join(line))
                        else:
                            self.cfgdata[line[0]] = line[1]
                    elif len(line) == 1:
                        self.cfgignore.append(line[0])
                    else:
                        pass

        except IOError:
            print("Exception opening file")
        except:
            print("Exception in config file")

    def printconfig(self):
        print("CONFIG PARAMETERS:")
        for key in self.cfgdata:
            print (key, self.cfgdata[key])
        if len(self.cfgignore) > 0:
            print("IGNORED in config file:")
            for line in self.cfgignore:
                print(line)


class App(tk.Tk):
    def __init__(self,Title,Geometry):
        super().__init__()
        self.title(Title)
        self.geometry(Geometry)

        self.textboxes = []

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

    def add_cfgtextbox(self,index,key,value):
        textbox = tk.Text(self, height=1, width=20)
        textbox.grid(row=index, column=1)
        textbox.insert(tk.END, key)
        self.textboxes.append(textbox)
        textbox = tk.Text(self, height=1, width=20)
        textbox.grid(row=index, column=2)
        textbox.insert(tk.END, value)
        self.textboxes.append(textbox)


    def button1_clicked(self):
        # T = tk.Text(self, height=2, width=20)
        self.text1.insert(tk.END, "longer.........text")

    def button2_clicked(self):
        # T = tk.Text(self, height=2, width=20)
        self.text2.insert(tk.END, "longer.........text")


if __name__ == '__main__':

    cfg = Programconfig("config.csv")
    cfg.readconfig()
    cfg.printconfig()




    app = App('myTitle','500x500')

    #app.create_texboxarray()


    for index, key in enumerate(cfg.cfgdata):
        print(index,key,cfg.cfgdata[key])
        # if key starts with # then....
        app.add_cfgtextbox(index+6,key,cfg.cfgdata[key])


    app.mainloop()

