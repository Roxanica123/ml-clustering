import plotly.express as px
import numpy as np

files = ["a.txt", "b.txt", "c.txt", "data.txt"]

for file in files:
    X = np.loadtxt('points/' + file, skiprows=1, usecols=range(2))
    labels = [x for x in range(1, len(X) + 1)]
    print(X)

    fig = px.scatter(X, x=0, y=1)
    fig.update_traces(marker=dict(size=20,
                                                             line=dict(width=2,
                                                                       color='#000000')))
    fig.write_image("./numerotate/{}.jpg".format(file[:-4]))
    fig.show()
