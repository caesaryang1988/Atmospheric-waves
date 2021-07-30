#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 16:17:39 2021

@author: hy337
"""

import xarray as xr
import cartopy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import matplotlib

dir = '//Users/hy337/Study/Research/Atmos_Sci_Proj/'

lat1, lat2 = 24, 50.5
lon1, lon2 = 240, 290
def lon360tolon180(lon):
    if lon > 180: return lon-360
    else: return lon
plon1, plon2 = lon360tolon180(lon1), lon360tolon180(lon2)
lev = 300

TP_data = xr.open_dataset(dir+'TP.nc')
N_time, N_latitude, N_longitude = np.shape(TP_data.tp)
new_latitude = TP_data.latitude[::-1]
TP_data = TP_data.assign_coords({'longitude':((TP_data.longitude+180)%360-180)})
new_longitude = xr.concat([TP_data.longitude[N_longitude//2:],TP_data.longitude[:N_longitude//2]], dim='longitude')

PV_data = xr.open_dataset(dir+'Pressure_level.nc')
PV_data = PV_data.assign_coords({'longitude':((PV_data.longitude+180)%360-180)})

def plotData_AblersEqualArea(time,lon,lat,C,Cf):
    extent = [-120, -70, 24, 50.5]
    central_lon = np.mean(extent[:2])
    central_lat = np.mean(extent[2:])

    lat = TP_tmp.latitude[:]
    lon = TP_tmp.longitude[:]
    tp = TP_tmp.tp[:,:]*1e3
    pv = PV_tmp.pv[:,:]

    cmap_name = 'Blues'
    levels = 11
    def modified_cm(cmap_name,levels):
        from matplotlib.colors import ListedColormap
        cmap = plt.cm.get_cmap(cmap_name,levels)
        newcolors = cmap(np.linspace(0,1,levels))
        newcolors[0] = np.array([1,1,1,1])
        mcmap = ListedColormap(newcolors)
        return mcmap
    mcmap = modified_cm(cmap_name, levels)
    
    plt.figure(figsize=(12, 6))
    ax = plt.axes(projection=ccrs.AlbersEqualArea(central_lon, central_lat))
    plt.contour(lon,lat,pv, levels = np.array([1e-6,4e-6,7e-6]), \
             transform=ccrs.PlateCarree(),linestyles='solid', \
            colors='black',linewidths=np.array([1,1.5,2]))
    plt.contour(lon,lat,pv, levels = np.array([-7e-6,-4e-6,-1e-6]), \
             transform=ccrs.PlateCarree(),linestyles='dashed', \
            colors='black',linewidths=np.array([2,1.5,1]))
    plt.contourf(lon,lat,tp,levels=np.linspace(0,10,11), \
             transform=ccrs.PlateCarree(), \
            cmap=mcmap, extend = 'max')
    cbar = plt.colorbar()
    cbar.ax.set_title(r"total precipitation [mm]")
    plt.title('Total precipitation (colors) and Potential Vorticity (contours) \n' + tstring)
    ax.add_feature(cartopy.feature.COASTLINE, edgecolor='grey')
    ax.add_feature(cartopy.feature.STATES, edgecolor='grey')
    ax.gridlines(color='lightgrey',linestyle='-',draw_labels=True)
    plt.savefig('tp-pv_'+tstring+'.pdf')
    plt.close()
    
def plotTimeSeries(x,ts1,ts2):
    fig, ax1 = plt.subplots()
    ax1.plot(x,ts1,'r-')
    ax1.set_ylabel('Total precipitation [mm]',color='r')
    ax1.tick_params(axis='y',color='r',labelcolor='r')
    plt.xticks(rotation=45,ha='right',rotation_mode='anchor')
    ax2 = ax1.twinx()
    ax2.plot(x,ts2,'b-')
    ax2.set_ylabel('Potential Vorticity',color='b')
    ax2.tick_params(axis='y',color='b',labelcolor='b')
    plt.savefig('tp-pv_ts.pdf')
    

for time in TP_data.time:
    time = pd.to_datetime(str(time.values))
    tstring = time.strftime('%Y-%m-%d_%HZ')
    TP_tmp = TP_data.sel(time=time,latitude=slice(lat2,lat1),longitude=slice(plon1,plon2))
    PV_tmp = PV_data.sel(time=time,latitude=slice(lat2,lat1),longitude=slice(plon1,plon2),level=lev)

    p_latitude = new_latitude.sel(latitude=slice(lat1,lat2))
    p_longitude = new_longitude.sel(longitude=slice(plon1,plon2))
    TP_tmp = TP_tmp.reindex({'latitude':p_latitude,'longitude':p_longitude})
    PV_tmp = PV_tmp.reindex({'latitude':p_latitude,'longitude':p_longitude})

    plotData_AblersEqualArea(tstring, p_longitude, p_latitude, PV_tmp, TP_tmp)

TP_ts = TP_data.tp.sel(latitude=slice(38,30),longitude=slice(-90,-80)).mean(axis=2).mean(axis=1)
PV_ts = PV_data.pv.sel(latitude=slice(40,25),longitude=slice(-105,-95),level=lev).mean(axis=2).mean(axis=1)
plotTimeSeries(TP_ts.time,TP_ts,PV_ts)
