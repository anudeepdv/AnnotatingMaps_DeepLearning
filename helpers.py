# -*- coding: utf-8 -*-
"""
@author: Dinesh
"""

import rasterio
import pandas as pd
import numpy as np
from rasterio import plot
import matplotlib.pyplot as plt


def return_indices(raster):
    np.seterr(divide='ignore', invalid='ignore')
    blue, green, red = raster[0], raster[1], raster[2]
    vre5, vre6, vre7 = raster[3], raster[4], raster[5]
    nir, vre8a, swir11, swir12 = raster[6], raster[7], raster[8], raster[9]
    
    # Initialize indices
    ndvi = np.empty(blue.shape, dtype=rasterio.float32)
    mndwi = np.empty(blue.shape, dtype=rasterio.float32)
    ndbi = np.empty(blue.shape, dtype=rasterio.float32)   
    
    # Checks
    check_mndwi = np.logical_or(swir11 > 0, red > 0)
    check_ndvi = np.logical_or(red > 0, nir > 0)
    check_ndbi = np.logical_or(swir11 > 0, nir > 0)
    
    # Calc indices
    ndvi = np.where(check_ndvi, (nir - red) / (nir + red), 0)
    mndwi = np.where(check_mndwi, (red - swir11) / (red + swir11), 0)
    ndbi = np.where(check_ndbi, (swir11 - nir) / (swir11 + nir), 0)
    
    # Normalize
    # mndwi = (mndwi - mndwi.min()) / (mndwi.max() - mndwi.min())
    # ndvi = (ndvi - ndvi.min()) / (ndvi.max() - ndvi.min())
    # ndbi = (ndbi - ndbi.min()) / (ndbi.max() - ndbi.min())
    return ndvi, mndwi, ndbi