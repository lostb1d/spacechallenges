from django.shortcuts import render, HttpResponse
from forestChangeDetection.forms import ImportGeojsonfileForm

import ee
ee.Initialize()
import os
# Create your views here.

def geojson_import(request):
    if request.method == "POST":
        form = ImportGeojsonfileForm(request.POST, request.FILES)
        if form.is_valid():
            geoJson = request.FILES['import_file']



def index(request):
    
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
        "tile" : getTile(geometry),
        "band_viz" : getVisParam(),
        # "form" : form,
        "title" : "Carbon Monoxide Emission",
        "startDate" : '2020-04-01',
        "endDate" : '2020-04-24',
    }

    return render(request,'index.html',context)

def getVisParam():
    viz_param = {
        "min" : 0.0,
        "max" : 0.4,
        "palette" : ['black','yellow'],
    }
    return viz_param

def getTile(geometry):
    transplanting = ee.ImageCollection('COPERNICUS/S2_SR').filterDate('2019-06-16','2019-07-15').median().clip(geometry).select('B8')
    harvesting = ee.ImageCollection('COPERNICUS/S2_SR').filterDate('2019-09-16','2019-10-15').median().clip(geometry).select('B8')
    pmi = index_calculation(harvesting , transplanting)
    viz_param = getVisParam()
    map_id_dict = ee.Image(pmi).getMapId(viz_param)
    tile = str(map_id_dict['tile_fetcher'].url_format)
    return tile

def index_calculation(a,b):
    return a.subtract(b).divide(a.add(b))