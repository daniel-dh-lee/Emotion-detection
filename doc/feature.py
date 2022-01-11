#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sklearn.metrics.pairwise
import numpy as np

def pairwise_dist(vec):
    dist  = sklearn.metrics.pairwise_distances(vec, metric='euclidean')
    np.fill_diagonal(dist, np.nan)
    return dist

def feature(fiducial_pt_list,index):
    pairwise_dist_feature = pairwise_dist(fiducial_pt_list[index]).flatten()
    pairwise_dist_feature = pairwise_dist_feature[~np.isnan(pairwise_dist_feature)]
    pairwise_dist_feature = np.append(pairwise_dist_feature,info['emotion_idx'][index])
    #pairwise_data  = cbind(pairwise_dist_feature, info['emotion_idx'][index])
    return pairwise_dist_feature


# In[ ]:




