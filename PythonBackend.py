import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN
from geopy.distance import great_circle
from shapely.geometry import MultiPoint
import os
import mplleaflet
from matplotlib import pyplot as plt
from matplotlib import cm


def get_hot_spots(max_distance,min_cases,coords):
    kms_per_radian=6371.0088
    epsilon=max_distance/kms_per_radian
    db=DBSCAN(eps=epsilon,min_samples=min_cases,algorithm='ball_tree',metric='haversine').fit(np.radians(coords))
    cluster_labels=db.labels_
    num_clusters=len(set(cluster_labels))
    clusters=pd.Series([coords[cluster_labels==n] for n in range(num_clusters)])
    lat=[]
    lon=[]
    num_members=[]
    for ii in range(len(clusters)):
        if clusters[ii].any():
            lat.append(MultiPoint(clusters[ii]).centroid.y)
            lon.append(MultiPoint(clusters[ii]).centroid.x)
            num_members.append(len(clusters[ii]))
    fig=plt.figure(figsize=(14,8))
    color_scale=np.log(num_members)
    ax=fig.add_subplot(111)
    plt.scatter(lat,lon,s=80,c=color_scale,cmap=cm.cool)
    mapfile='JustForDemo.html'
    mplleaflet.show(path=mapfile)

def readFile():
    f=open('META.txt')
    fname=f.readline()
    fname=fname[0:len(fname)-1]
    mdist=f.readline()
    mdist=mdist[0:len(mdist)-1]
    mcas=f.readline()
    max_distance=float(mdist)
    min_cases=float(mcas)
    df=pd.read_csv(fname)
    coords=df[['Lat','Lon']].to_numpy()
    get_hot_spots(max_distance,min_cases,coords)

if __name__ == "__main__":
    readFile()