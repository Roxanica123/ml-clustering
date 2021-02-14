##############################################################################################
###                             K-Means Python Implementation                              ###
###    http://konukoii.com/blog/2017/01/15/5-min-tutorial-k-means-clustering-in-python/    ###
##############################################################################################

import random
import math
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import plotly.graph_objects as go


# Euclidian Distance between two d-dimensional points
def eucldist(p0, p1):
    dist = 0.0
    for i in range(0, len(p0)):
        dist += (p0[i] - p1[i]) ** 2
    return math.sqrt(dist)


# K-Means Algorithm
def kmeans(k, p_points, p_centroids, file):
    # d - Dimensionality of Datapoints
    d = len(p_points[0])

    # Limit our iterations
    Max_Iterations = 1000
    i = 0

    cluster = [0] * len(p_points)
    prev_cluster = [-1] * len(p_points)

    # Randomly Choose Centers for the Clusters
    cluster_centers = p_centroids
    pic = 1
    while (cluster != prev_cluster) or (i > Max_Iterations) or (force_recalculation):
        prev_cluster = list(cluster)
        force_recalculation = False
        i += 1
        # Update Point's Cluster Alligiance
        for p in range(0, len(p_points)):
            min_dist = float("inf")

            # Check min_distance against all centers
            for c in range(0, len(cluster_centers)):

                dist = eucldist(p_points[p], cluster_centers[c])

                if (dist < min_dist):
                    min_dist = dist
                    cluster[p] = c  # Reassign Point to new Cluster

        # Update Cluster's Position
        for k in range(0, len(cluster_centers)):
            new_center = [0] * d
            members = 0
            for p in range(0, len(p_points)):
                if (cluster[p] == k):  # If this point belongs to the cluster
                    for j in range(0, d):
                        new_center[j] += p_points[p][j]
                    members += 1

            for j in range(0, d):
                if members != 0:
                    new_center[j] = new_center[j] / float(members)

                    # This means that our initial random assignment was poorly chosen
                # Change it to a new datapoint to actually force k clusters
                else:
                    new_center = random.choice(p_points)
                    force_recalculation = True
                    print
                    "Forced Recalculation..."

            cluster_centers[k] = new_center

        colors = ["#0000FF", "#00FF00", "#FF0066"]
        cluster_colors = ["#000077", "#007400"]
        fig = go.Figure()
        for i in range(len(p_points)):
            fig.add_trace(
                go.Scatter(
                    mode='markers',
                    x=[int(p_points[i][0])],
                    y=[int(p_points[i][1])],
                    marker=dict(
                        color=colors[cluster[i]],
                        size=20,
                        line=dict(width=2,
                                  color='#000000')
                    )
                )
            )
        for i in range(len(cluster_centers)):
            fig.add_trace(
                go.Scatter(
                    mode='markers',
                    x=[cluster_centers[i][0]],
                    y=[cluster_centers[i][1]],
                    marker=dict(
                        color=cluster_colors[i],
                        size=20,
                        line=dict(width=2,
                                  color='#000000')
                    )
                )
            )
        fig.layout.update(showlegend=False)
        print(pic)
        fig.write_html("./kmeans/{}/{}.html".format(file[:-4], pic))
        fig.show()
        pic += 1


# TESTING THE PROGRAM#
files = ["a.txt", "b.txt", "c.txt", "data.txt"]

if __name__ == "__main__":
    # 2D - Datapoints List of n d-dimensional vectors. (For this example I already set up 2D Tuples)
    # Feel free to change to whatever size tuples you want...
    for file in files:
        points = X = np.loadtxt('points/' + file, skiprows=1, usecols=range(2))
        k_means = KMeans(n_clusters=2,
                         init='random',
                         n_init=1,
                         random_state=90, max_iter=1).fit(points)
        centroids = k_means.cluster_centers_
        k = 2  # K - Number of Clusters
        kmeans(k, points, centroids, file)
