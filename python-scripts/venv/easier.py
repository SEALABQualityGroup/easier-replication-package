# Libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from math import pi

# Set data
# df = pd.DataFrame({
# 'group': ['A','B','C','D'],
# 'var1': [38, 1.5, 30, 4],
# 'var2': [29, 10, 9, 34],
# 'var3': [8, 39, 23, 24],
# 'var4': [7, 31, 33, 14],
# 'var5': [28, 15, 32, 14]
# })
repository = "/mnt/store/research/easier/worse-to-better/ew_20200617_2000_eb_20200627_1640/referenceFront/"
csv_files = ["1018", "1087", "2113", "3577", "1481"]
perf_qs = ["34.7", "35", "34.9", "33", "33"]
print(csv_files)

#f = plt.figure()
for j in range(0, len(csv_files)):
    data = pd.read_csv(repository + csv_files[j] + "_Length_4_CloningWeight_1.5_MaxCloning_3.csv", sep=";")
    #print(data.head())

    arr = np.array([
        data.delta_perf_q,
        data.changes,
        data.pas
    ], dtype=np.float)


    # Scaling changes and pas
    lengths = np.linalg.norm(arr, axis=-1)
    arr[lengths > 0] = arr[lengths > 0] / lengths[lengths > 0][:, np.newaxis]
    changes = (arr[1]/abs(arr[1]).max()) /100
    pas = (arr[2]/abs(arr[2]).max()) /100

    delta_perf_q = data.delta_perf_q  # arr[0]#/abs(arr[0]).max()

    df = pd.DataFrame({
    'group': range(0, len(data)),
    'perfq': delta_perf_q,
    'changes': changes,
    'pas': pas
    })

    # number of variable
    categories = list(df)[1:]
    N = len(categories)

    # We are going to plot the first line of the data frame.
    # But we need to repeat the first value to close the circular graph:
    # values = df.loc[0].drop('group').values.flatten().tolist()
    # values += values[:1]
    # values

    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    # Initialise the spider plot
    #ax = plt.subplot(111, polar=True)
    #ax = f.subplot(2,2,j+1, polar=True)
    #ax = plt.subplot(3,2,j+1, polar=True)
    ax = plt.subplot(111, polar=True)
    #ax = f.add_subplot(2,2,j+1, polar=True)

    #ax.set_rasterized(True)
    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories, color='grey', size=8)
    # plt.title(csv_files[j] + " -> perfQ(FTA) = -" + perf_qs[j] + "%")

    # Draw ylabels
    ax.set_rlabel_position(0)
    #plt.yticks([-0.10, 0, 0.005, 0.01, 0.015], [-0.010, 0, 0.005, 0.01, 0.015], color="grey", size=7)
    min_perfq = min(delta_perf_q)
    max_perfq = max(delta_perf_q)
    plt.yticks(color="grey", size=7)
    plt.ylim(min_perfq, max_perfq)

    for i in range(len(data)):
        values=df.loc[i].drop('group').values.flatten().tolist()
        values += values[:1]
        label = '[{:+.2f}% {} {}]'.format((data.delta_perf_q[i]*100), data.changes[i], data.pas[i])
        ax.plot(angles, values, linewidth=1, linestyle='solid', label=label)
        ax.fill(angles, values, alpha=0.1)
    plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1), title="[perfq, changes, pas]", fontsize="small", title_fontsize="small")
    f = plt.gcf()
    #f.set_size_inches(10, 10)
    plt.savefig(
        "/home/peo/git/papers/work_in_progress/2020_easier_journal/figures/radar-" + csv_files[j] + ".pdf",
        rasterized=True, format='pdf', dpi=300, bbox_inches='tight')
    plt.show()
    plt.clf()
#f = plt.gcf()
#f.set_size_inches(10, 10)
#plt.savefig("/home/peo/git/papers/work_in_progress/2020_easier_journal/figures/worse-better.pdf", rasterized=True, format='pdf', dpi=300, bbox_inches='tight')
#plt.show()
#f = plt.figure()
print("Done")
