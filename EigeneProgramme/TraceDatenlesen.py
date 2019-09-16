import matplotlib.pyplot as plt
import datetime as dt
from collections import defaultdict

kurvenDaten = defaultdict(list)
SpaltenNamen = []

# Funktion für Spaten


def SpaltenBenennen(DateinameSpalten):
    # Datei mit Spaltenangebe öffnen und in eine Liste eintragen
    with open(DateinameSpalten, 'r') as f_SpaltenNamen:
        for zeile in f_SpaltenNamen:
            name = zeile.split('\,')
            SpaltenNamen.append(name)

    # alle nicht benötigten Zeichen entfernen
    for n in range(len(SpaltenNamen)):
        replaceChar_1 = ' '
        replaceChar_2 = '\\n'
        text = str(SpaltenNamen[n])
        for char in text:
            text = text.replace(replaceChar_1, '')
            text = text.replace(replaceChar_2, '')
        SpaltenNamen[n] = text


def TraceDaten(DateinameTrace):
    with open(DateinameTrace, 'r') as f_kurvenDaten:
        for zeile in (3, f_kurvenDaten):
            datumStr, value = zeile.split(';')
            ZeitStempel = (dt.datetime.strptime(
                datumStr, '%d.%m.%Y %H:%M:%S:%MS')).timestamp()
            kurvenDaten[ZeitStempel].append(value)


SpaltenBenennen('EigeneProgramme\TraceDaten\spalten.txt')
TraceDaten('EigeneProgramme\TraceDaten\WaageA_TestProd_01.txt')

print(SpaltenNamen)
print(len(SpaltenNamen))
