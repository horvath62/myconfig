
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
                        self.cfgdata[line[0]] = line[1]
                        if line[0][0] == "#":
                            self.cfgignore.append(' '.join(line))
                        else:
                            pass

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
        self.textbox_key = {}
        self.textbox_value = {}
        self.buttoncomment = []
        self.checkcomment = []

        self.label1 = tk.Label(self, text="Hello")
        self.label2 = tk.Label(self, text="Parameter")
        self.label1.grid(row = 0, column = 0, pady = 2)
        self.label2.grid(row=0, column=1, pady=2)
        self.check1 = tk.Checkbutton(self)
        self.check1.grid(row=1, column=0)
        self.button1 = tk.Button(self, text='Click Me')
        self.button1['command'] = self.button1_clicked
        self.button1.grid(row = 2, column = 1)
        self.buttonsave = tk.Button(self, text='SAVE')
        self.buttonsave['command'] = self.buttonsave_clicked
        self.buttonsave.grid(row = 2, column = 2)




    def add_cfgtextbox(self,index,key,value):

        print(">>",index, key, value)

        rowoffset = 6
        textbox = tk.Text(self, height=1, width=20)
        textbox.grid(row=index+rowoffset, column=2)
        textbox.insert(tk.END, key)
        self.textbox_key[index] = textbox
        textbox = tk.Text(self, height=1, width=20)
        textbox.grid(row=index+rowoffset, column=3)
        textbox.insert(tk.END, value)
        self.textbox_value[index] = textbox


    def button1_clicked(self):
        # parameter from text boxes
        for index in range(len(self.textbox_key)):
            print("###", index, self.textbox_key[index].get(1.0, "end-1c"),self.textbox_value[index].get(1.0, "end-1c"))
            # self.textbox_value[index])

    def buttonsave_clicked(self):
        # save parameters
        pass

        try:
            with open(self.cfgfile, "w") as filehandle:

                for index in range(len(self.textbox_key)):
                    filehandle.writelines(self.textbox_key[index].get(1.0, "end-1c"),",",
                          self.textbox_value[index].get(1.0, "end-1c"))
                    # self.textbox_value[index])
                    filehandle.close()

        except IOError:
            print("Exception opening file")
        except Exception as e:
            print("Exception in config file:",e)







if __name__ == '__main__':

    cfg = Programconfig("config.csv")
    cfg.readconfig()
    cfg.printconfig()




    app = App('myTitle','500x500')

    #app.create_texboxarray()


    for index, key in enumerate(cfg.cfgdata, start=0):
        print("==>",index,key,cfg.cfgdata[key])
        # if key starts with # then....
        app.add_cfgtextbox(index,key,cfg.cfgdata[key])


    app.mainloop()

