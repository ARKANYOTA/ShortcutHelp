import sys
import os
import time
from Get import getkey
import json
import os.path



def get():
    key = getkey()
    if key=="\x03":
        exit()
    return key

class Menus:
    nb = 0  # Nombres de menus
    allname = []
    allcolor = []
    selectmenu = 0 
    class Infos:
        "Donne les infos d'un menu"
        def __init__(self, name, color, files):  # files=*.json  color=\033[*m && type=int
            
            Menus.nb = Menus.nb + 1
            Menus.allname += [name]
            Menus.allcolor += [color]
            Menus.Infos.files = files

        def loadDataFile(self):
            if os.path.isfile(self.files):
                with open(self.files) as f:
                    self.Data = json.load(f)
            else:
                self.Data = {} 

        def countOfLines(self):
            print(self.countDicoLines(self.Data))

        def countDicoLines(self, data):
            nblines = 0
            for key, i in data.items():
                if type(i)==dict:
                    nblines+= self.countDicoLines(i)
                nblines+=1
            return nblines



    def __init__(self):
        pass
    def affichermenu(self, x):
        # bar = ""
        # for i in self.allname:
        #     bar += "|"+ (x//self.nb-2)*"-" +"|"
        # barMenu = "\033[1;1H\033[33m"
        # bar += str(self.nb)
        
        #print(bar)
        #return self.allname, self.nb, x, self.selectmenu
        
        bar = "\033[1;1H"
        it = 0
        for i in self.allname:
            if it==self.selectmenu:
                color = 0
            else:
                color =  self.allcolor[it]
            bar += "\033["+str(color)+"m"+ (i) +(x//self.nb-len(i))*" " +"\033[0m"
            it +=1
        # barMenu = "\033[1;1H\033[33m"
        # bar += str(self.selectmenu)

        return bar
    def selectright(self):
        self.selectmenu = (self.selectmenu + 1)%self.nb
    def selectleft(self):
        self.selectmenu = (self.selectmenu - 1)%self.nb
    @classmethod
    def nombresMenu(cls):
        Menus.nb
# sys.stdout.write("\x1b]2;Pythoni3help\x07")
ancx,ancy = 0,0

# CREATION MENU
menu = Menus()
# iHelp = menu.Infos("help", 42)
ii3wm = menu.Infos("i3wm", 43, "i3wm.json")
#ilinux = menu.Infos("linux", 44)

# Clear All
print("\033[2J")

while True:
    x, y = os.get_terminal_size()
    key = get()
    if key=="d":
        pass
    elif key=="\x1b[C": # Right
        menu.selectright()
    elif key=="\x1b[D": # Right
        menu.selectleft()
    

    print(menu.affichermenu(x))
    ancx,ancy = x,y
    # print("hellp", x, y, x==ancx, y==ancy) # Menus.renvoyer())
    ii3wm.loadDataFile()
    ii3wm.countOfLines()
input()
