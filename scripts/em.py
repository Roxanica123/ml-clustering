import argparse
import sys
import numpy as np
import pandas as pd
from sklearn.mixture import GaussianMixture
import plotly.graph_objects as go


def init_parser():
    parser = argparse.ArgumentParser(description="none")
    parser.add_argument('--iterations', '-i', default=5, type=str,
                        help="The number of iterations")
    return parser


def func(file):
    parser = init_parser()
    args = parser.parse_args(sys.argv[1:])
    i = int(args.iterations)
    data = np.loadtxt('points/' + file, skiprows=1, usecols=range(2))
    gmm = GaussianMixture(n_components=2, random_state=2, max_iter=100, verbose=2, init_params="kmeans")
    gmm.fit(data)
    num_iterations = gmm.n_iter_

    for i in range(1, num_iterations + 1):
        data = np.loadtxt('points/'+file, skiprows=1, usecols=range(2))
        gmm = GaussianMixture(n_components=2, random_state=2, max_iter=i, verbose=2, init_params="kmeans")
        gmm.fit(data)
        labels = gmm.predict(data)
        frame = pd.DataFrame(data)
        frame['cluster'] = labels
        frame.columns = ['X', 'Y', 'cluster']
        color = ['blue', 'green']
        fig = go.Figure()
        for k in range(0, 2):
            data = frame[frame["cluster"] == k]
            fig.add_trace(
                go.Scatter(
                    mode='markers',
                    x=data["X"],
                    y=data["Y"],
                    marker=dict(
                        color=color[k],
                        size=20,
                        line=dict(width=2,
                                  color='#000000')
                    ),
                    name='\u00B5 = {} , \u03C3 = {}'.format(gmm.means_[k, :], gmm.covariances_[k, :])
                )
            )
        fig.add_trace(
            go.Scatter(
                mode='markers',
                x=[0],
                y=[0],
                opacity=0,
                name='\u03C0 = {}'.format(gmm.weights_[1])
            )
        )
        fig.layout.update(legend=dict(
            orientation="h"))
        fig.write_image("em/{}/{}.jpg".format(file[:-4], i))


files = ["a.txt", "b.txt", "c.txt", "data.txt"]
for file in files:
    func(file)