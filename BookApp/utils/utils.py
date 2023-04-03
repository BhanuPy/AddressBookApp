#utils/utils.py
"""
utils.py

This module contains utility function such as:

get_distance : Calculates the distance between two coordinates in latitute and longitude

"""

from math import sin, cos, sqrt, atan2, radians


def get_distance(lat1, lon1, lat2, lon2):
    R = 6373.0  # approximate radius of the Earth in km

    lat1_rad = radians(lat1)
    lon1_rad = radians(lon1)
    lat2_rad = radians(lat2)
    lon2_rad = radians(lon2)

    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad

    a = sin(dlat / 2)**2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance_km = R * c
    return distance_km
