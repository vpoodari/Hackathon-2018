#Authors: Vinay C. Poodari & Dixon Hofflet 
#This program was designed for the parsing of a BRCA data held in a TSV file and plot the data into an easy to understand format. 
#This project is for the MLH 2018 Hackathon held at UCSC.
import sys
import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import numpy as np
import pandas as pd
import numpy as np


def getData():
    brca1 = []
    brca2 = []
    labels = ['VariantName', 'Freq', 'Prior']
    brca1_rows = []
    brca2_rows = []
    with sys.stdin as inputFile:
        inputFile.readline()
        for line in inputFile:
            x = line.rstrip().split(' ')
            if x[1] == '\"BRCA1\"':
                brca1.append( (x[2], np.float(x[3]), np.float(x[4])) )
                brca1_rows.append(x[2])
            else:
                brca2.append( (x[2], np.float(x[3]), np.float(x[4])) )
                brca2_rows.append(x[2])


    b2 = pd.DataFrame.from_records(brca2,  columns=labels)
    b1 = pd.DataFrame.from_records(brca1, columns=labels)

    return b1,b2
#VarientName, Freq, Prior
b1,b2 = getData()
fig_width=7
fig_height=7
plt.figure(figsize=(fig_width,fig_height))
VariantName = '"NM_007294.3:c.-192T>C"'
panel_width=2/7
panel_height=2/7
panel1=plt.axes([0.1,0.1,panel_width,panel_height])
panel1.set_ylim(0, 1)
panel1.set_xlim(0,1)
panel1.set_xticks(['Freq', 'Prior'])

panel1.tick_params(axis='both',which='both',\
                   bottom='off', labelbottom='off',\
                   left='off', labelleft='off')

panel2=plt.axes([0.5,0.1,panel_width,panel_height])
panel2.set_ylim(1, 0)
panel2.set_xlim(0, 1)
for i in range (0, len(b1['VariantName'])):
    if b1['VariantName'][i] != VariantName:
        panel2.scatter(b1['Freq'][i], b1['Prior'][i], s =2 , color ='black', linewidth=0, marker='o')
    else:
        panel1.bar(0.1, b1['Freq'][i], width = 0.3)
        panel1.bar(0.5, b1['Prior'][i], width = 0.3)
        color = 'red' 
        panel2.scatter(b1['Freq'][i], b1['Prior'][i], s =13 , color =color, linewidth=0, marker='o')

panel2.tick_params(axis='both',which='both',\
                   bottom='off', labelbottom='off',\
                   left='off', labelleft='off')


plt.savefig('data.png', dpi = 600)