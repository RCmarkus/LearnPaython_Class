import matplotlib.pyplot as plt
import datetime as dt
from collections import defaultdict

kurvenDaten = []
SpaltenNamen = []

# Funktion für Spaten


def DateiBereinigen(Dateiname, ListName, SplitChar=None, oldChar_1=None, oldChar_2=None, oldChar_3=None, replaceByChar=None):
    # Datei mit Spaltenangebe öffnen und in eine Liste eintragen
    with open(Dateiname, 'r') as f:
        for zeile in f:
            Value = zeile.split(SplitChar)
            ListName.append(Value)

    # alle nicht benötigten Zeichen entfernen
    for n in range(len(ListName)):
        text = str(ListName[n])
        for char in text:
            text = text.replace(oldChar_1, replaceByChar)
            if not oldChar_2 == None:
                text = text.replace(oldChar_2, replaceByChar)
            if not oldChar_3 == None:
                text = text.replace(oldChar_3, replaceByChar)
        ListName[n] = text


""" 
def TraceDaten(DateinameTrace):
    with open(DateinameTrace, 'r') as f_kurvenDaten:

        for zeile in (3, f_kurvenDaten):
            datumStr = zeile.split('\ ;')
            ZeitStempel = (dt.datetime.strptime(
                datumStr, '%d.%m.%Y %H:%M:%S:%MS')).timestamp()


            for n in range(1, 74):
                value = []
                value[n] = n.split('\;')
            kurvenDaten[ZeitStempel].append(value)

 """

DateiBereinigen('EigeneProgramme\TraceDaten\spalten.txt', SpaltenNamen,
                SplitChar='\,', oldChar_1=' ', oldChar_2='\\n', replaceByChar='')
DateiBereinigen('EigeneProgramme\TraceDaten\WaageA_TestProd.txt', kurvenDaten,
                SplitChar='\;', oldChar_1=' ', oldChar_2='\\x00', oldChar_3='\\n', replaceByChar='')
# TraceDaten('EigeneProgramme\TraceDaten\WaageA_TestProd.txt')

print(SpaltenNamen)
print(len(SpaltenNamen))

print(kurvenDaten)
print(len(kurvenDaten))
