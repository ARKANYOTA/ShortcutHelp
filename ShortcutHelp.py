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
    files = []
    selectmenu = 0 
    class Infos:
        "Donne les infos d'un menu"
        def __init__(self, name, color, files):  # files=*.json  color=\034[*m && type=int
            
            Menus.nb = Menus.nb + 1
            Menus.allname += [name]
            Menus.Infos.name = name
            Menus.allcolor += [color]
            Menus.files += [files]
    def loadDataFile(self):
        if os.path.isfile(self.getNameFile()):
            with open(self.getNameFile()) as f:
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

    def getNameFile(self):
        return self.files[self.selectmenu]

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
                color = 4 
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

# sys.stdout.write("\x1b]2;Pythoni3help\x07")
ancx,ancy = 0,0

# CREATION MENU
menu = Menus()
iHelp = menu.Infos("help", 42, "mml.json")
ii3wm = menu.Infos("i3wm", 43, "i3wm.json")
ilinux = menu.Infos("linux", 44, "help.json")

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
    print("\033[2J") 

    print(menu.affichermenu(x))  # Barre de menu
    # TODO print(menu.trioptions(x,y))  # Todo Barre d'option tout en bas
    # print("hellp", x, y, x==ancx, y==ancy) # Menus.renvoyer())
    menu.loadDataFile()  # Charge les données du document sélectionner
    print(menu.Data)  # return Dico Infos
    menu.countOfLines()  # print Le nombres de lignes dans self.Data
    
    """
    ii3wm.loadDataFile()
    ii3wm.countOfLines()
    ilinux.loadDataFile()
    ilinux.countOfLines()
    """
    # POUR LE MOMENT PAS BESOIN
    # ancx,ancy = x,y
input()
