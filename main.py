
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
        print("Program Config")
    def readconfig(self):
        try:
            self.cfgdata = {}
            self.cfgignore = {}
            with open(self.cfgfile, "r") as filehandle:
                for line in csv.reader(filehandle):
                    # print(line)
                    # print(len(line))
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

    def writeconfig(self,config,cfgfile):
        try:
            with open(self.cfgfile, "w") as filehandle:
                for line in config:
                    filehandle.write(line)
                    print(line)
        except:
            print("Exception in write")

class App(tk.Tk):
    def __init__(self, title, cfgfile, Geometry):
        super().__init__()
        self.cfgfile = cfgfile
        self.title(title)
        self.geometry(Geometry)

        self.textbox_key = {}
        self.textbox_value = {}
        self.label_index = {}
        self.newcfg = {}

        self.labelfilename = tk.Label(self, text="Config file:"+cfgfile)
        self.labelfilename.grid(row = 0, column = 0, columnspan= 2)
        self.check1 = tk.Checkbutton(self)
        self.check1.grid(row=0, column=0)
        self.insert = tk.Button(self, text='INSERT NEW CONFIG')
        self.insert['command'] = self.buttoninsert_clicked
        self.insert.grid(row = 2, column = 1)
        self.buttonsave = tk.Button(self, text='SAVE')
        self.buttonsave['command'] = self.buttonsave_clicked
        self.buttonsave.grid(row = 2, column = 2)
        self.buttonread = tk.Button(self, text='READ')
        self.buttonread['command'] = self.buttonread_clicked
        self.buttonread.grid(row = 2, column = 0)


    def add_cfgtextbox(self,index,key,value):

        print(">>",index, key, value)

        rowoffset = 6
        label = tk.Label(self, text=index)
        label.grid(row=index+rowoffset, column=0)
        self.label_index[index] = label
        textbox = tk.Text(self, height=1, width=20)
        textbox.grid(row=index+rowoffset, column=1)
        textbox.insert(tk.END, key)
        self.textbox_key[index] = textbox
        textbox = tk.Text(self, height=1, width=20)
        textbox.grid(row=index+rowoffset, column=2)
        textbox.insert(tk.END, value)
        self.textbox_value[index] = textbox

    def create_textboxes(self):
        for index, key in enumerate(cfg.cfgdata, start=0):
            print("==>", index, key, cfg.cfgdata[key])
            app.add_cfgtextbox(index, key, cfg.cfgdata[key])

    def get_textboxes(self):
        print("TextBoxes count:",len(self.textbox_key))
        self.newcfg = {}
        for index in range(len(self.textbox_key)):

            #print("get", index, self.textbox_key[index].get(1.0, "end-1c"))
            key = self.textbox_key[index].get(1.0, "end-1c")
            value = self.textbox_value[index].get(1.0, "end-1c")
            print("get:",key,value)
            if len(key) > 0:
                print("###", index, key, value)
                self.newcfg[key] = value

    def buttoninsert_clicked(self):
        # parameter from text boxes
        pass
        print("len of textbox_key",len(self.textbox_key))
        self.add_cfgtextbox(len(self.textbox_key),"","")

    def buttonsave_clicked(self):
        # save parameters
        print("SAVE EVENT")
        self.get_textboxes()
        print(self.newcfg)
        pass
        try:
            with open(self.cfgfile, "w") as filehandle:
                for key in self.newcfg:
                    keyvalue = key+","+self.newcfg[key]
                    filehandle.write(keyvalue+"\n")
                    print(keyvalue)
        except:
            print("Exception in write")
        filehandle.close()

        # Read config from file
        print("READ EVENT")
        global cfg
        cfg.readconfig()
        cfg.printconfig()

        self.textbox_init()
        self.create_textboxes()

    def textbox_init(self):
        # first destroy the text boxes before reading in new
        textbox_count = len(self.textbox_key)
        for index in range(textbox_count):
            self.textbox_key[index].destroy()
            self.textbox_value[index].destroy()
            self.label_index[index].destroy()
        self.textbox_key = {}
        self.textbox_value = {}
        self.label_index = {}
        self.textbox_key = {}
        self.textbox_value = {}
        self.label_index = {}
        self.newcfg = {}

    def buttonread_clicked(self):
        # Read config from file
        print("READ EVENT")
        global cfg
        cfg.readconfig()
        cfg.printconfig()

        self.textbox_init()
        self.create_textboxes()




if __name__ == '__main__':

    cfg = Programconfig("config.csv")
    cfg.readconfig()
    cfg.printconfig()

    print(cfg.cfgfile)

    app = App("LineMaker", cfg.cfgfile, '500x500')
    app.create_textboxes()

    '''
    for index, key in enumerate(cfg.cfgdata, start=0):
        print("==>",index,key,cfg.cfgdata[key])
        app.add_cfgtextbox(index,key,cfg.cfgdata[key])
    '''

    app.mainloop()

