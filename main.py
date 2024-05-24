
import csv
import tkinter as tk


# PRE-LOADING CONFIGURATION PARAMETERS
# A config with comma separated parameters are loaded from file
# parameters are in pairs on each line as: <key,value> (i.e. START,2024)
# After editing in GUI and then saved back to config:
# If key is blank, then that parameter is not saved
# If value is blank, it is saved with as such (i.e.  key,)
# If three or more CSV, then only first two are saved as key,value

class Programconfig:
    def __init__(self, configfile):
        # A List of words
        self.cfgdata = {}
        self.cfgfile = configfile
        self.cfgignore = []

    def readconfig(self):
        try:
            self.cfgdata = {}
            self.cfgignore = {}
            with open(self.cfgfile, "r") as filehandle:
                for line in csv.reader(filehandle):
                    # print("read:",line)
                    if len(line) > 1:
                        self.cfgdata[line[0]] = line[1]
                    elif len(line) == 1:
                        self.cfgdata[line[0]] = ""
                        self.cfgignore.append(line[0])
                    else:
                        pass
                filehandle.close()

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
        print()

    def writeconfig(self,config):
        try:
            with open(self.cfgfile, "w") as filehandle:
                for line in config:
                    filehandle.write(line)
                    print(line)
        except:
            print("Exception in write")

class App(tk.Tk):
    def __init__(self, title, cfgfile, cfgdata, Geometry):
        super().__init__()
        self.cfgfile = cfgfile
        self.title(title)
        self.geometry(Geometry)

        self.textbox_key = {}
        self.textbox_value = {}
        self.label_index = {}
        self.cfgdata = cfgdata
        self.newcfg = {}

        self.check1 = tk.Checkbutton(self)
        self.check1.grid(row=1,column=0)
        self.check2 = tk.Checkbutton(self)
        self.check2.grid(row=2, column=0)
        self.check3 = tk.Checkbutton(self)
        self.check3.grid(row=3, column=0)



        self.labelfilename = tk.Label(self, text="Config file:")
        self.labelfilename.grid(row = 0, column = 2)

        self.buttonsave = tk.Button(self, text='SAVE')
        self.buttonsave['command'] = self.buttonsave_clicked
        self.buttonsave.grid(row = 0, column = 1)
        self.buttonread = tk.Button(self, text='READ')
        self.buttonread['command'] = self.buttonread_clicked
        self.buttonread.grid(row = 0, column = 0)





        self.label1 = tk.Label(self, text="Check1",anchor="w")
        self.label1.grid(row=1, column=1)





        self.textboxcfgfile= tk.Text(self, height=1, width=20)
        self.textboxcfgfile.grid(row=0, column=3)
        self.textboxcfgfile.insert(tk.END, self.cfgfile)

        self.button10 = tk.Button(self, text='GO', pady=10)
        self.button10['command'] = self.button10_clicked
        self.button10.grid(row = 4, column = 0, pady = 10)

        self.button11 = tk.Button(self, text='Button11', pady=10)
        self.button11['command'] = self.button11_clicked
        self.button11.grid(row = 4, column = 1)

        self.button12 = tk.Button(self, text='Button12', pady=10)
        self.button12['command'] = self.button12_clicked
        self.button12.grid(row = 4, column = 2)

        self.button13 = tk.Button(self, text='Button13', pady=10)
        self.button13['command'] = self.button13_clicked
        self.button13.grid(row = 4, column = 3)

        self.button21 = tk.Button(self, text='Button21', pady=10)
        self.button21['command'] = self.button21_clicked
        self.button21.grid(row = 5, column = 1)

        self.button22 = tk.Button(self, text='Button22', pady=10)
        self.button22['command'] = self.button22_clicked
        self.button22.grid(row = 5, column = 2)

        self.button23 = tk.Button(self, text='Button23', pady=10)
        self.button23['command'] = self.button23_clicked
        self.button23.grid(row = 5, column = 3)

        # Set the offset for the starting row of the dynamic text input fields below the buttons.
        self.rowoffset = 7

    def button10_clicked(self):
        pass

    def button11_clicked(self):
        pass

    def button12_clicked(self):
        pass

    def button13_clicked(self):
        pass

    def button21_clicked(self):
        pass

    def button22_clicked(self):
        pass

    def button23_clicked(self):
        pass

    def textbox_init(self):
        # first destroy the text boxes before reading in new
        textbox_count = len(self.textbox_key)
        # print(self.textbox_key.keys())
        for index in range(textbox_count):
            self.textbox_key[index].destroy()
            self.textbox_value[index].destroy()
            self.label_index[index].destroy()
            # print("destroyed:",index)
            pass
        self.buttoninsert.destroy()

        self.textbox_key = {}
        self.textbox_value = {}
        self.label_index = {}
        self.newcfg = {}


    def create_textboxes(self):
        for index, key in enumerate(self.cfgdata, start=0):
            # print("==>", index, key, self.cfgdata[key])
            self.add_cfgtextbox(index, key, self.cfgdata[key])

        self.buttoninsert = tk.Button(self, text='INSERT')
        self.buttoninsert['command'] = self.buttoninsert_clicked
        self.buttoninsert.grid(row = self.rowoffset+len(self.textbox_key), column = 0, pady=5)


    def add_cfgtextbox(self,index,key,value):
        # print(">>",index, key, value)
        label = tk.Label(self, text=index)
        label.grid(row=index+self.rowoffset, column=1)
        self.label_index[index] = label
        textbox = tk.Text(self, height=1, width=20)
        textbox.grid(row=index+self.rowoffset, column=2)
        textbox.insert(tk.END, key)
        self.textbox_key[index] = textbox
        textbox = tk.Text(self, height=1, width=20)
        textbox.grid(row=index+self.rowoffset, column=3)
        textbox.insert(tk.END, value)
        self.textbox_value[index] = textbox
        # print("create:",index,key,value)

    def get_textboxes(self):
        # print("TextBoxes count:",len(self.textbox_key))
        self.newcfg = {}
        for index in range(len(self.textbox_key)):

            # print("get", index, self.textbox_key[index].get(1.0, "end-1c"))
            key = self.textbox_key[index].get(1.0, "end-1c")
            value = self.textbox_value[index].get(1.0, "end-1c")
            # print("###", index, key, value)
            if key in self.newcfg:
                print("Duplicate Key:"+key+ "cant have duplicate keys")
                pass

            elif len(key) > 0:
                # print("len(key)>0t:",index, key,value)
                self.newcfg[key] = value

            else:
                pass
                # print("POP:",index)

    def buttoninsert_clicked(self):
        self.add_cfgtextbox(len(self.textbox_key),"","")
        self.buttoninsert.grid(row = self.rowoffset+len(self.textbox_key), column = 0, pady=5)

    def buttoncommit_clicked(self):
        pass

    def buttonsave_clicked(self):
        # save parameters into file
        self.get_textboxes()
        # print(self.newcfg)
        filename = self.textboxcfgfile.get(1.0, "end-1c")
        print("SAVING CONFIG FILE:",filename)
        try:
            with open(filename, "w") as filehandle:
                for key in self.newcfg:
                    keyvalue = str(key)+","+str(self.newcfg[key])+"\n"
                    filehandle.write(keyvalue)
                    # print(keyvalue)
        except e:
            print("Exception in write",e)
        filehandle.close()

        # Read config back from file just saved
        filename = self.textboxcfgfile.get(1.0, "end-1c")
        cfg = Programconfig(filename)
        cfg.readconfig()
        cfg.printconfig()
        self.cfgdata = cfg.cfgdata
        self.textbox_init()
        self.create_textboxes()

    def buttonread_clicked(self):
        # Read config from file
        filename = self.textboxcfgfile.get(1.0, "end-1c")
        print("READING CONFIG FILE:",filename)
        cfg = Programconfig(filename)
        cfg.readconfig()
        cfg.printconfig()
        self.cfgdata = cfg.cfgdata
        self.textbox_init()
        self.create_textboxes()



if __name__ == '__main__':

    cfg = Programconfig("config.csv")
    cfg.readconfig()
    cfg.printconfig()

    # print(cfg.cfgfile)

    app = App("Program Config", cfg.cfgfile, cfg.cfgdata, '600x400')
    app.create_textboxes()

    app.mainloop()

