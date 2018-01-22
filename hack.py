#Authors: Vinay C. Poodari, Dixon Hofflet, Justin Hofflet, Andrew Blair 
#This program was designed for the parsing of a BRCA data held in a TSV file and plot the data into an easy to understand format. 
#This project is for the MLH 2018 Hackathon held at UCSC.
#run with  python hack.py BRCA_variant_data\ \(1\).tsv "NM_007294.3:c.-192T>C" 1 uses sys.argv, "Varient name" #gene number

import sys
import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import numpy as np
import pandas as pd
import numpy as np

def getData():
    """
    This method is used to get data from the TSV file. 
    """
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
    #returns certain data frame 
    data = sys.argv[3]
    if data == '1':
        return b1
    else:
        return b2
#VarientName, Freq, Prior
dframe = getData()
#deciding figure size
fig_width=12
fig_height=12
plt.figure(figsize=(fig_width,fig_height))
VariantName = '"'+sys.argv[2]+'"'
#setting panel heights 
panel_width=4/10
panel_height=4/10
#setting panel sizes
panel2=plt.axes([0.3,0.55,panel_width,panel_height])
panel2.set_ylim(0, 1)
panel2.set_ylabel('Prior')
panel2.set_yticks(np.arange(0,1.1, 0.1))
panel2.set_xticks(np.arange(0,1.1, 0.1))
panel2.set_xlabel('Freq')
panel2.set_xlim(1, 0)
panel2.set_title("Prior vs Freq")
for i in range (0, len(dframe['VariantName'])):
    if dframe['VariantName'][i] != VariantName:
        panel2.scatter(dframe['Freq'][i], dframe['Prior'][i], s =9 , color ='black', linewidth=0, marker='o')
    else:
        panel1=plt.axes([0.3,0.05,panel_width,panel_height])
        panel1.set_title("Your Varient")
        panel1.set_ylim(0, 1)
        stuff = ['Freq', 'Prior']
        panel1.bar([0.3, 0.7], [dframe['Freq'][i], dframe['Prior'][i]] ,  width = 0.3, color = ['purple', 'pink'], tick_label = ['Freq: '+str(round(dframe['Freq'][i],2)), \
            'Prior '+ str(round(dframe['Prior'][i],2))])
        color = 'red'
        panel2.scatter(dframe['Freq'][i], dframe['Prior'][i], color =color, linewidth=0, marker= 'X')

panel2.tick_params(axis='both',which='both',\
                   bottom='on', labelbottom='on',\
                   left='on', labelleft='on')

plt.savefig('data.png', dpi = 600)