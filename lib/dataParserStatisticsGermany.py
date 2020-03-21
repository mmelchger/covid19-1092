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

# Load Hospital Data for Regions in Germany
fieldnames = ["Date", "ID", "Name", "numHospitals", "numBeds",
              "Augenheilkunde",
              "chirurgie",
              "Gynaekologie",
              "HNO",
              "Dermatologie",
              "Innere",
              "Geriatrie",
              "Kinder",
              "Neurologie",
              "Orthopaedie",
              "Urologie",
              "Andere",
              "KinderPsy",
              "Psy",
              "PsyTherapie"]
hospitalList = []
with open(hospitalPath, "r", encoding="ISO-8859-15") as f:
    readObj = csv.DictReader(f, fieldnames=fieldnames, delimiter=";")
    # Skip Header
    for i in range(8):
        next(readObj)
    for row in readObj:
        hospitalList.append(row)

# Create Region Objects and store Population Data
regionList = []
for iRegion, iArea, iHospital in zip(populationDensityList, areaList,
                                     hospitalList):
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
    assert iRegion["ID"] == iHospital["ID"]
    newRegion.PopulationTotal    = int(iRegion["Gesamt"].replace("-","0").replace(".", "0"))
    newRegion.PopulationMale     = int(iRegion["Maennlich"].replace("-", "0").replace(".", "0"))
    newRegion.PopulationFemale   = int(iRegion["Weiblich"].replace("-", "0").replace(".", "0"))
    newRegion.RegionIDZensus     = iRegion["ID"]
    newRegion.ValidPopulation    = not "-" in iRegion.values()
    newRegion.ValidPopulation    = not "." in iRegion.values()
    areaSplit = iArea["Area"].split(",")
    if len(areaSplit) == 1:
        newRegion.Area           = int(iArea["Area"].replace("-", "0"))
        newRegion.ValidArea      = False
    else:
        newRegion.Area           = float(areaSplit[0] + "." + areaSplit[1])
    newRegion.numHospitals       = int(iHospital["numHospitals"].replace("-", "0"))
    newRegion.numBeds            = int(iHospital["numBeds"].replace("-", "0"))
    newRegion.Augenheilkunde     = int(iHospital["Augenheilkunde"].replace("-", "0"))
    newRegion.Chirurgie          = int(iHospital["chirurgie"].replace("-", "0"))
    newRegion.Gynaekologie       = int(iHospital["Gynaekologie"].replace("-", "0"))
    newRegion.HNO                = int(iHospital["HNO"].replace("-", "0"))
    newRegion.Dermatologie       = int(iHospital["Dermatologie"].replace("-", "0"))
    newRegion.Innere             = int(iHospital["Innere"].replace("-", "0"))
    newRegion.Geriatrie          = int(iHospital["Geriatrie"].replace("-", "0"))
    newRegion.Kinderheilkunde    = int(iHospital["Kinder"].replace("-", "0"))
    newRegion.Neurologie         = int(iHospital["Neurologie"].replace("-", "0"))
    newRegion.Orthopaedie        = int(iHospital["Orthopaedie"].replace("-", "0"))
    newRegion.Urologie           = int(iHospital["Urologie"].replace("-", "0"))
    newRegion.Andere             = int(iHospital["Andere"].replace("-", "0"))
    newRegion.KinderPsy          = int(iHospital["KinderPsy"].replace("-", "0"))
    newRegion.Psy                = int(iHospital["Psy"].replace("-", "0"))
    newRegion.PsyTherapie        = int(iHospital["PsyTherapie"].replace("-", "0"))
    newRegion.ValidHospital      = not "-" in iHospital.values()
    regionList.append(newRegion)

# Store Area Data

    










