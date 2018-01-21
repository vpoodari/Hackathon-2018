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
    inputFile =open(sys.argv[1], 'r')

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
    data = sys.argv[3]
    if data == '1':
        return b1
    else:
        return b2
#VarientName, Freq, Prior
dframe = getData()
fig_width=10
fig_height=10
plt.figure(figsize=(fig_width,fig_height))
VariantName = '"NM_007294.3:c.-192T>C"'
#VariantName = '"'+sys.argv[2] + '"'
panel_width=3/10
panel_height=3/10
panel2=plt.axes([0.5,0.1,panel_width,panel_height])
panel2.set_ylim(0, 1)
panel2.set_ylabel('Prior')
panel2.set_yticks(np.arange(0,1.1, 0.1))
panel2.set_xticks(np.arange(0,1.1, 0.1))
panel2.set_xlabel('Freq')
panel2.set_xlim(1, 0)
for i in range (0, len(dframe['VariantName'])):
    if dframe['VariantName'][i] != VariantName:
        panel2.scatter(dframe['Freq'][i], dframe['Prior'][i], s =2 , color ='black', linewidth=0, marker='o')
    else:
        panel1=plt.axes([0.1,0.2,panel_width,panel_height])
        panel1.set_ylim(0, 1)
        print([dframe['Freq'][i], dframe['Prior'][i]])
        stuff = ['Freq', 'Prior']
        panel1.bar([0.3, 0.7], [dframe['Freq'][i], dframe['Prior'][i]] ,  width = 0.3, color = ['blue', 'orange'], tick_label = ['Freq', 'Prior'])
        color = 'cyan' 
        panel2.scatter(dframe['Freq'][i], dframe['Prior'][i], s =13 , color =color, linewidth=0, marker='o')

panel2.tick_params(axis='both',which='both',\
                   bottom='on', labelbottom='on',\
                   left='on', labelleft='on')




plt.savefig('data.png', dpi = 600)