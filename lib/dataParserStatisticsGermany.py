#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 11:11:59 2020

@author: enno
"""
import os
import requests
import csv
from utils import region

# Load Data for Corona Infections
urlCoronaData   = r"https://pomber.github.io/covid19/timeseries.json"
response        = requests.get(urlCoronaData)
coronaData      = response.json()

# Path to Statistical Data for Regions in Germany
path                    = r"../data/"
populationDensityFile   = r"12411-01-01-4.csv"
areaFile                = r"11111-01-01-4.csv"
hospitalFile            = r"23111-01-04-4.csv"
populationPath          = os.path.join(path, populationDensityFile)
areaPath                = os.path.join(path, areaFile)
hospitalPath            = os.path.join(path, hospitalFile)

# Load Population Data for Regions in Germany
fieldnames              = ["ID", "Name", "Gesamt", "Maennlich", "Weiblich"]
populationDensityList   = []
with open(populationPath, "r", encoding="ISO-8859-15") as f:
    readObj = csv.DictReader(f, fieldnames=fieldnames, delimiter=";")
    # Skip Header
    for i in range(8):
        next(readObj)
    for row in readObj:
        populationDensityList.append(row)

# Load Area of Regions in Germany
fieldnames              = ["Date", "ID", "Name", "Area"]
areaList                = []
with open(areaPath, "r", encoding="ISO-8859-15") as f:
    readObj = csv.DictReader(f, fieldnames=fieldnames, delimiter=";")
    # Skip Header
    for i in range(6):
        next(readObj)
    for row in readObj:
        areaList.append(row)

# Create Region Objects and store Population Data
regionList = []
for iRegion, iArea in zip(populationDensityList, areaList):
    if iRegion["ID"] == "DG":
        country = iRegion["Name"].strip()
        newRegion = region(country)
    elif len(str(iRegion["ID"])) == 2:
        province = iRegion["Name"].strip()
        newRegion = region(country, province)
    elif iRegion["Name"] is None:
        break
    else:
        newRegion = region(country, province, iRegion["Name"].strip())
    assert iRegion["ID"] == iArea["ID"]
    newRegion.PopulationTotal  = iRegion["Gesamt"]
    newRegion.PopulationMale   = iRegion["Maennlich"]
    newRegion.PopulationFemale = iRegion["Weiblich"]
    newRegion.RegionIDZensus   = iRegion["ID"]
    newRegion.Area             = iArea["Area"]
    regionList.append(newRegion)

# Store Area Data

    










