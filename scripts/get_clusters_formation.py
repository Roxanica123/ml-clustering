import numpy as np
import pandas as pd
import plotly.graph_objects as go
from sklearn.cluster import AgglomerativeClustering

files = ["a.txt", "b.txt", "c.txt", "data.txt"]
linkages = ["average", "single", "complete", "ward"]
colors = ['#b9a319', '#312579', '#3c4e10', '#ad6740', '#f2ec44', '#bc66ac', '#0f7ec9', '#c42382',
          '#33406c', '#a53f90', '#0fa80f', '#7dea54', '#8d149a', '#0ceff4', '#ec0d9e', '#3d9d3c', '#77d3b6',
          '#0c2467',
          '#30d725', '#e3ed80', '#8e6823', '#1cf7ae', '#5090f6', '#f10b35', '#c68fee', '#07989f', '#83873d',
          '#8c4e25',
          '#af3bca', '#645ac2', '#7d1b95', '#0a2b42', '#178453', '#7b8b7d', '#3228be', '#9ae632', '#4b33a4',
          '#b1d8fb',
          '#c3ffeb', '# d7062c', '#8b0fa8', '#6035e6', '#20e91d', '#37192e', '#cfcf5c', '#ae3a4e', '#d7b682',
          '#f6fbf9',
          '#ab33ae', '#c6a07d', '#5b7fe2', '#3a714b', '#d8ece2', '#4e9b11', '#2115e9', '#61287f', '#c73862',
          '#8408f1',
          '#17bbbc', '#b10781', '#983cc4', '# c4837a', '#c12a65', '#dd069a', '#e2c55e', '#421627', '#585105',
          '#095e35',
          '#51e6f2', '#bf5cd2', '#a8846c', '#343210', '#fe79fd', '#77482a']


def draw(file_p, linkage_p, data_p, labels, i, points_colors):
    fig = go.Figure()
    cluster_colors = []
    for aux in set(labels):
        cluster_colors.append(point_colors[list(labels).index(aux)])
    for point in range(len(labels)):
        color_index = labels[point]
        fig.add_trace(
            go.Scatter(
                mode='markers',
                x=[data_p["X"][point]],
                y=[data_p["Y"][point]],
                marker=dict(
                    color=cluster_colors[color_index],
                    size=20,
                    line=dict(width=2,
                              color='#000000')
                )
            )
        )
    fig.layout.update(showlegend=False)
    fig.write_html("./clustere_formare/{}/{}/{}.html".format(file_p[:-4], linkage_p, i))
    print(file[:-4], linkage)


for file in files:
    X = np.loadtxt("points/" + file, skiprows=1, usecols=range(2))
    data = pd.DataFrame(X, columns=["X", "Y"])
    max_clusters = len(data)
    for linkage in linkages:
        point_colors = [colors[i] for i in range(max_clusters)]
        for i, number in enumerate(range(2, max_clusters, 2)):
            cluster = AgglomerativeClustering(n_clusters=number, affinity='euclidean', linkage=linkage)
            cluster.fit_predict(data)
            draw(file, linkage, data, cluster.labels_, i + 1, point_colors)

        # for linkage in linkages:
