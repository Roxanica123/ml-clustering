import plotly.figure_factory as ff
import scipy.cluster.hierarchy as sch
import numpy as np

files = ["a.txt", "b.txt", "c.txt", "data.txt"]

for file in files:
    X = np.loadtxt("./points/" + file, skiprows=1, usecols=range(2))
    labels = [x for x in range(1, len(X) + 1)]
    fig = ff.create_dendrogram(X, color_threshold=100, linkagefun=lambda x: sch.linkage(x, "single"), labels=labels)
    fig.update_layout(width=1000, height=800)
    fig.write_html("./dendrograms/{}_dendrogram_single.html".format(file[:-4]))

    fig = ff.create_dendrogram(X, color_threshold=400, linkagefun=lambda x: sch.linkage(x, "average"), labels=labels)
    fig.update_layout(width=1000, height=800)
    fig.write_html("./dendrograms/{}_dendrogram_average.html".format(file[:-4]))

    fig = ff.create_dendrogram(X, color_threshold=400, linkagefun=lambda x: sch.linkage(x, "complete"), labels=labels)
    fig.update_layout(width=1000, height=800)
    fig.write_html("./dendrograms/{}_dendrogram_complete.html".format(file[:-4]))

    fig = ff.create_dendrogram(X, color_threshold=400, linkagefun=lambda x: sch.linkage(x, "ward", metric="euclidean"),
                               labels=labels)
    fig.update_layout(width=1000, height=800)
    fig.write_html("./dendrograms/{}_dendrogram_ward.html".format(file[:-4]))

