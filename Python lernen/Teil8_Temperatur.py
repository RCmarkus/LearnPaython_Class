import matplotlib.pyplot as plt
import datetime as dt
from collections import defaultdict

tageswert = defaultdict(list)

with open('Python lernen\Teil_08_Temperatur_Draußen Temp_2.txt', 'r') as f:
    for zeile in f:
        datumStr, t = zeile.split('\t')
        datum = (dt.datetime.strptime(datumStr, '%d.%m.%Y %H:%M:%S')).date()
        t = float(t)
        tageswert[datum].append(t)

tagMax = []
tagMin = []
tagDatum = []
for key in tageswert:
    heigtTemp = max(tageswert[key])
    lowTemp = min(tageswert[key])

    if abs(heigtTemp) < 40 and abs(lowTemp) < 40:
        tagMax.append(max(tageswert[key]))
        tagMin.append(min(tageswert[key]))
        tagDatum.append(key)

fig, ax = plt.subplots()
ax.plot(tagDatum, tagMax, lw=1, label='Hi', color='red')
ax.plot(tagDatum, tagMin, lw=1, label='Low', color='blue')
ax.fill_between(tagDatum, tagMax, tagMin,
                facecolor='orange', alpha=0.2, label='range')
ax.grid(linestyle='-.', linewidth='0.5', color='green')
ax.legend()
plt.yticks([-10, 0, 25, 30, 35, 40])
plt.show()
