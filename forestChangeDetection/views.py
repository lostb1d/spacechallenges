from django.shortcuts import render, HttpResponse
from forestChangeDetection.forms import ImportGeojsonfileForm

import ee
ee.Initialize()
import os
from datetime import date , timedelta
from datetime import datetime
from dateutil.parser import parse
import pandas as pd
import pygeoj
import json
# from django.conf.settings import PROJECT_ROOT
# Create your views here.

def index(request):
    coord=''
    if request.method == "POST":
        form = ImportGeojsonfileForm(request.POST, request.FILES)
        if form.is_valid():
            geoJson = request.FILES['import_file']
            data = json.load(geoJson)
            a = pygeoj.load(None,data)
            for feature in a:
                coord = feature.geometry.coordinates
                gtype = feature.geometry.type
                print(gtype)
    # file_ = open(os.path.join(PROJECT_ROOT, 'filename'))
    form = ImportGeojsonfileForm()
    if(coord!=''):
        geometry = ee.Geometry.MultiPolygon(coord)
    else:
        geometry = ee.Geometry.Polygon([[[84.97873462030498, 27.87424989960898],
            [84.74527514764873, 27.563032482426987],
            [85.20670092889873, 27.385144636789754],
            [85.69833911249248, 27.368071821574812],
            [85.95102465936748, 27.57277145564543],
            [86.04166186639873, 27.840253798218345],
            [85.70657885858623, 27.973748526646474],
            [85.55826342889873, 27.95676744082692],
            [85.29733813592998, 27.910662458572368]]])

    context = {
        # "tile2020" : getTile2020(geometry),
        "tile2019" : getTile2019(geometry),
        "tile2018" : getTile2018(geometry),
        "tile2017" : getTile2017(geometry),
        "band_viz" : getVisParam(),
        # "form" : form,
        "title" : "Carbon Monoxide Emission",
        "startDate" : '2020-04-01',
        "endDate" : '2020-04-24',
        "form":form,
    }

    return render(request,'index.html',context)

def getVisParam():
    viz_param = {
        "min" : 0.0,
        "max" : 0.4,
        "palette" : ['black','yellow'],
    }
    return viz_param

def getTile2017(geometry):
    transplanting = ee.ImageCollection('LANDSAT/LC08/C01/T1_RT').filterDate('2017-06-16','2017-07-15').mosaic().clip(geometry).select('B8')
    print(transplanting)
    harvesting = ee.ImageCollection('LANDSAT/LC08/C01/T1_RT').filterDate('2017-09-16','2017-10-15').mosaic().clip(geometry).select('B8')
    pmi = index_calculation(harvesting , transplanting)
    viz_param = getVisParam()
    map_id_dict = ee.Image(pmi).getMapId(viz_param)
    tile = str(map_id_dict['tile_fetcher'].url_format)
    print("Tile")
    print(tile)
    return tile

def getTile2018(geometry):
    transplanting = ee.ImageCollection('LANDSAT/LC08/C01/T1_RT').filterDate('2018-06-16','2018-07-15').mosaic().clip(geometry).select('B8')
    harvesting = ee.ImageCollection('LANDSAT/LC08/C01/T1_RT').filterDate('2018-09-16','2018-10-15').mosaic().clip(geometry).select('B8')
    pmi = index_calculation(harvesting , transplanting)
    viz_param = getVisParam()
    map_id_dict = ee.Image(pmi).getMapId(viz_param)
    tile = str(map_id_dict['tile_fetcher'].url_format)
    return tile

def getTile2019(geometry):
    transplanting = ee.ImageCollection('LANDSAT/LC08/C01/T1_RT').filterDate('2019-06-16','2019-07-15').median().clip(geometry).select('B8')
    harvesting = ee.ImageCollection('LANDSAT/LC08/C01/T1_RT').filterDate('2019-09-16','2019-10-15').median().clip(geometry).select('B8')
    pmi = index_calculation(harvesting , transplanting)
    viz_param = getVisParam()
    map_id_dict = ee.Image(pmi).getMapId(viz_param)
    tile = str(map_id_dict['tile_fetcher'].url_format)
    return tile

# def getTile2020(geometry):
#     transplanting = ee.ImageCollection('COPERNICUS/S2_SR').filterDate('2020-06-16','2020-07-15').median().clip(geometry).select('B8')
#     harvesting = ee.ImageCollection('COPERNICUS/S2_SR').filterDate('2020-09-16','2020-10-15').median().clip(geometry).select('B8')
#     pmi = index_calculation(harvesting , transplanting)
#     viz_param = getVisParam()
#     map_id_dict = ee.Image(pmi).getMapId(viz_param)
#     tile = str(map_id_dict['tile_fetcher'].url_format)
#     return tile

def index_calculation(a,b):
    return a.subtract(b).divide(a.add(b))