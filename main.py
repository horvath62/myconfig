
import csv


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


if __name__ == '__main__':
    print("Program Config")
    cfg = Programconfig("config.csv")
    cfg.readconfig()

