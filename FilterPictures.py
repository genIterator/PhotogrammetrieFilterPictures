######################
# Filter Pictures
# Ver 0.1
# Python 3.4
#
# Input a selector (divisor) to select corresponding pictures.
# These pictures will be copied into a new "output" folder
# Script needs to be in the same folder as the pictures.
#
######################

import sys
import optparse
import glob
import os
import shutil

# global stuff...
dateiEndung = ""
selector = 1
zahlenStellen = 3


def readDateiEndung ():
    tempEndung = ""
    weiter = True
    global dateiEndung
    while (weiter):
        tempEndung = input("Bitte die dateiEndung der auszuwählenden Bilddateien angeben (z.B. .jpeg):")
        tempE = "*"+tempEndung
        if glob.glob(tempE):
            dateiEndung = tempEndung
            weiter = False
            print(dateiEndung)
            print("dateiEndung wurde auf "+dateiEndung+" festgelegt.")
            return True
        else:
            print("Dateityp im aktuellen Ordner nicht gefunden.")

def readSelector():
    tempSelector = ""
    tempSelectorInt = -1
    weiter = True
    global selector
    while (weiter):
        tempSelector = input("Bitte den Selector angeben. z.B. 2 für jedes zweite Bild:")
        tempSelector = tempSelector.strip()
        try:            
            tempSelectorInt = int(tempSelector)
            if tempSelectorInt >= 2:
                selector = tempSelectorInt
                weiter = False
                print("Selector wurde auf "+tempSelector+" festgelegt.")
                return True
            else:
                print("Der Selector muss >= 2 sein.")
        except:
            print("Keine valide Zahl eingegeben.")
        
            
def readStellen ():
    tempStellen = ""
    tempStellenInt = -1
    weiter = True
    global zahlenStellen
    
    while (weiter):
        tempStellen = input("Bitte die Anzahl der Zahlenstellen angeben. z.B: 3 bei Dateiname452.jpg:")
        tempStellen = tempStellen.strip()
        try:
            tempStellenInt = int(tempStellen)
            if tempStellenInt >= 1:
                zahlenStellen = tempStellenInt
                weiter = False
                print("Stellen wurde auf "+tempStellen+" festgelegt.")
                return True
            else:
                print("Die Anzahl der Stellen muss mindestens 1 betragen.")
        except:
            print("Keine valide Zahl angegeben.")
            
            

def readUserInput ():
    readDateiEndung()
    readSelector()
    #readStellen()
    return True

def copyFiles (dateienSelected):
    tempSrc = ""
    tempDest = ""
    tempDest2 = ""
    dest = ""
    val = 0
    
    if (os.name is "nt"):
        tempDest = "\output"
    else:
        tempDest = "/output"       
    #find new output folder
    tempDest2 = tempDest    
    while (os.path.isdir(os.getcwd() + tempDest)):
        val +=1
        tempDest = tempDest2+str(val)              
    dest = os.getcwd() + tempDest
    try:
        os.makedirs(dest)
    except:
        print("output Ordner konnte nicht erstellt werden. Möglicherweise fehlende Schreibrechte.")
        return False        
    print("Dateien werden nach "+dest+" kopiert.")
    for datei in dateienSelected:
        shutil.copy(datei, dest)
    print("Alle Dateien kopiert. Vorgang abgeschlossen.")
    return True
    
    

def selectPictures ():
    global dateiEndung
    global zahlenStellen
    global selector
    dateiName = None
    dateiZahl = ""
    selec = zahlenStellen*-1
    tempGlob = "*"+dateiEndung
    zahl = 0
    dateienSelected = []
    cont = "j"
    
    for datei in glob.glob(tempGlob):
        dateiName = os.path.splitext(datei)[0]
        dateiZahl = dateiName[selec:]
        dateiZahl = dateiZahl.lstrip("0")

        try:
            zahl = int(dateiZahl)
            if (zahl % selector == 0):
                dateienSelected.append(datei)
        except:
            print("Fehler bei der Konvertierung von: "+dateiZahl)
            
    print(str(len(dateienSelected))+" Dateien selektiert")
    cont = input("Fortfahren (j/n)? Dateien im output Ordner werden ggf. überschrieben!")
    if (cont.lower() == "j"):
        if (copyFiles(dateienSelected)):
            return True
        else:
            return False
    else:
        print("Vorgang abgebrochen.")
        return False
    
def selectPictures2 ():
    global dateiEndung
    global selector
    counter = 0
    dateienSelected = []
    tempGlob = "*"+dateiEndung
    cont = " "    
    
    for datei in glob.glob(tempGlob):
        counter += 1
        if (counter % selector == 0):
            dateienSelected.append(datei)
    print(str(len(dateienSelected))+" Dateien selektiert")
    cont = input("Fortfahren (j/n)? Dateien im output Ordner werden ggf. überschrieben!")
    if (cont.lower() == "j"):
        if (copyFiles(dateienSelected)):
            return True
        else:
            return False
    else:
        print("Vorgang abgebrochen.")
        return False
        
    
    

def main(argv=None):
    if argv is None:
        argv = sys.argv
    readUserInput()
    selectPictures2()
    sys.exit()

if __name__ == "__main__":
    main()