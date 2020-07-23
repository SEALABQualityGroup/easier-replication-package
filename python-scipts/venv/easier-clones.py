# Libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sb
from math import pi

repository = "/home/peo/git/papers/work_in_progress/2020_easier_journal/R-scripts/"
csv_files = ['nsga-clones', 'spea-clones']

dtypes = {
    "WSN": np.int32,
    "CHN": np.int32,
    "FTA": np.int32,
    "LAN": np.int32,
    "DB": np.int32,
    "DSK": np.int32,
    "SCR": np.int32,
}

for j in range(0, len(csv_files)):
    df = pd.read_csv(repository + csv_files[j] + ".csv", sep=";",
                     dtype=dtypes, index_col=0)
    # Use row names as labels
    labels = df.columns.values
    colors = sb.color_palette("Set1", n_colors=len(labels))

    for label in labels:
        df.at['Total', label] = df[label].sum()

    plt.rcParams['font.size'] = 24
    f, ax = plt.subplots()
    ax.pie(df.loc['Total'], autopct='%.0f%%', startangle=90, colors=colors, pctdistance=0.85)
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    #ax.legend(loc='center', title="AEmilia AEI", labels=labels, fontsize=15, title_fontsize=18)
    for i in range(0, len(df.loc['Total'])):
        print(df.loc['Total'][i])
        print(sum(df.loc['Total']))
        print((df.loc['Total'][i] / sum(df.loc["Total"]))*100)
    ax.legend( loc='center', title="AEmilia AEI", labels=['%s (%.0f%%)' % (l, (df.loc['Total'][s] / sum(df.loc["Total"]))*100) for l, s in zip(labels, range(0, len(df.loc['Total'])))])
    f = plt.gcf()
    f.set_size_inches(10, 10)
    plt.savefig("/home/peo/git/papers/work_in_progress/2020_easier_journal/figures/piechart-" + csv_files[j] + ".pdf",rasterized=True, format='pdf', dpi=300, bbox_inches='tight')

# plt.tight_layout()
#plt.show()
