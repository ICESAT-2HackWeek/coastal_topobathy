# -*- coding: utf-8 -*-
"""
Generic GIS tools.

"""
import numpy as np


def deg2rad(deg):
    return deg * (np.pi / 180)


def dist_latlon2meters(lat1, lon1, lat2, lon2):
    """Returns the distance between two coordinate points - (lon1, lat1) and (lon2, lat2) along the earth's surface in
    meters.

    Refactored from contributors/NoelleHelder/AK_topobathy_vis.ipynb by @nkhelder
    """
    R = 6371000
    dlat = deg2rad(lat2 - lat1)
    dlon = deg2rad(lon2 - lon1)
    a = np.sin(dlat / 2) * np.sin(dlat / 2) + np.cos(deg2rad(lat1)) * np.cos(deg2rad(lat2)) * np.sin(dlon / 2) * np.sin(dlon / 2)
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    return R * c
