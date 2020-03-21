 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 01:00:42 2020

@author: enno
"""
import datetime
import os
import csv
from collections import namedtuple
import requests

class region():
    """
    Region object.
    """

    def __init__(self, aCountry, aProvince=None, aCity=None):
        """
        Create Region object.
        """
        # Empty Init
        self.Province   = aProvince
        self.Country    = aCountry
        self.City       = aCity  # auch: Landkreis
        self.Lat        = None
        self.Long       = None
        
        self.ValidArea          = True
        self.ValidHospital      = True
        self.ValidPopulation    = True

        self.PopulationDensity  = None
        self.PopulationTotal    = None
        self.PopulationMale     = None
        self.PopulationFemale   = None
        self.RegionIDZensus     = None
        self.TimeSeries         = None
        self.TimeSeriesStart    = None
        self.Area               = None
        
        self.numHospitals       = None
        self.numBeds            = None
        self.Augenheilkunde     = None
        self.Chirurgie          = None
        self.Gynaekologie       = None
        self.HNO                = None
        self.Dermatologie       = None
        self.Innere             = None
        self.Geriatrie          = None
        self.Kinderheilkunde    = None
        self.Neurologie         = None
        self.Orthopaedie        = None
        self.Urologie           = None
        self.Andere             = None
        self.KinderPsy          = None
        self.Psy                = None
        self.PsyTherapie        = None

        self.Action             = None
    
    
    def printInfo(self):
        """Print Members."""
        print("===== Members of Region ====")
        print("Country: ", self.Country)
        print("Province: ", self.Province)
        print("City: ", self.City)
        print("Population Density per km²: ", self.PopulationDensity)
        print("Total Population: ", self.PopulationTotal)
        print("Male Population: ",  self.PopulationMale)
        print("Female Population: ", self.PopulationFemale)
        print("Area in km²: ", self.Area)
        print("Number of Hospitals: ", self.numHospitals)
        print("Number of Hospital Beds: ", self.numBeds)
        print("Number of Beds in Augenheilkunde: ", self.Augenheilkunde)
        print("Number of Beds in Chirurgie: ", self.Chirurgie)
        print("Number of Beds in Gynäkologie: ", self.Gynaekologie)
        print("Number of Beds in HNO: ", self.HNO)
        print("Number of Beds in Dermatologie: ", self.Dermatologie)
        print("Number of Beds in Innere Medizin: ", self.Innere)
        print("Number of Beds in Geriatrie: ", self.Geriatrie)
        print("Number of Beds in Kinderheilkunde: ", self.Kinderheilkunde)
        print("Number of Beds in Neurologie: ", self.Neurologie)
        print("Number of Beds in Orthopaedie: ", self.Orthopaedie)
        print("Number of Beds in Urologie: ", self.Urologie)
        print("Number of Beds in Andere: ", self.Andere)
        print("Number of Beds in Kinder Psychologie: ", self.KinderPsy)
        print("Number of Beds in Psychologie: ", self.Psy)
        print("Number of Beds in Psycho Therapie: ", self.PsyTherapie)

    def get_name(self):
        """Get Name of Province."""
        if self.Province is None:
            raise UserWarning("No data set for Name/Province")
        return self.Province
    
    def get_country(self):
        """Get Name of Country."""
        if self.Country is None:
            raise UserWarning("No data set for Country")
        return self.Country


    def get_NumberInfected(self, aDatetime):
        """
        Get Number of infected Persons at date aDatetime

        Parameters
        ----------
        datetime : TYPE
            DESCRIPTION.

        returns
        -------
        int Total Number of Infected Persons at Datetime including recovered 
            Persons

        """
        raise NotImplementedError("get_NumberInfected is not yet implemented")
        #TODO: implement
    
    
    def get_NumberDead(self, aDatetime):
        """
        Get Number of Persons died at Day Datetime.

        Parameters
        ----------
        aDatetime : TYPE
            DESCRIPTION.

        Returns
        -------
        int:
            Total Number of Persons Dead at Datetime

        """
        raise NotImplementedError("get_NumberDead is not yet implemented")
        #TODO: Implement


    def get_NumberRecovered(self, aDatetime):
        """
        Get Number of Persons died at Day Datetime.

        Parameters
        ----------
        aDatetime : TYPE
            DESCRIPTION.

        Returns
        -------
        int:
            Total Number of Persons recovered

        """
        raise NotImplementedError("get_NumberRecovered is not yet implemented")
        #TODO: Implement


    def set_timeSeries(self, aDataset):
        """
        Set Time Series Data for Region

        Parameters
        ----------
        aDataset : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        raise NotImplementedError("set_timeSeries is not yet implemented")
        #TODO: implement


    def set_action(self, aBegin, aName, aEnd=None):
        """
        Set Maßnahme in Region.

        Parameters
        ----------
        aBegin : datetime.date object
            Date of Begin of Action
        aName : string
            Name to identify
        aEnd : datetime.date object, optional
            same type as Begin

        Returns
        -------
        None.

        """
        assert type(aBegin) == datetime.date
        assert type(aName) == str
        if self.Action is None:
            self.Action = []
        Massnahme = namedtuple("Massnahme", ["Begin", "End", "Name"])
        self.Action.append(Massnahme(aBegin, aEnd, aName))
    
    
    def set_populationDensity(self, aDensity):
        """
        Set membervariable Population Density of Region.

        Parameters
        ----------
        aDensity : float
            Citizen per square kilometer

        Returns
        -------
        None.

        """
        self.PopulationDensity = aDensity


def parseCountryData():
    path = r"../doc/"
    laenderActionsFile = r"Länderdaten_Corona_Maßnahmen.csv"
    laenderAdditionalInfoFile = r"Länderdaten_Corona.csv"
    LaenderAction = os.path.join(path, laenderActionsFile)
    laenderAdd = os.path.join(path, laenderAdditionalInfoFile)
    
    countryInfo = []
    with open(LaenderAction, "r") as f:
        readObj = csv.DictReader(f)
        for row in readObj:
            countryInfo.append(row)
    countries = [elem["Country"] for elem in countryInfo]
    
    additionalInfo = []
    with open(laenderAdd, "r") as f:
        readObj = csv.DictReader(f)
        for row in readObj:
            additionalInfo.append(row)
    countriesAdd = [elem["Country"] for elem in additionalInfo]
    
    # Load Data for Corona Infections
    urlCoronaData   = r"https://pomber.github.io/covid19/timeseries.json"
    response        = requests.get(urlCoronaData)
    coronaData      = response.json()
    
    countryList = []
    for index, key in enumerate(list(coronaData.keys())):
        newCountry              = region(key)
        newCountry.TimeSeries   = coronaData[key]
        startdate               = coronaData[key][0]["date"]
        date                    = startdate.split("-")
        newCountry.TimeSeriesStart = datetime.date(int(date[0]),
                                                   int(date[1]),
                                                   int(date[2]))
        if key in countries:
            i = countries.index(key)
            if not countryInfo[i]["School closure (localised)"] == "":
                beginSchoolLocal        = countryInfo[i]["School closure (localised)"]
                schoolLocal             = beginSchoolLocal.split("/")
                newCountry.set_action(datetime.date(int("20"+schoolLocal[2]),
                                                int(schoolLocal[0]),
                                                int(schoolLocal[1])),
                                  "School_closure_localised")
            if not countryInfo[i]["School closure (national)"] == "":
                beginSchoolNational     = countryInfo[i]["School closure (national)"]
                schoolNational          = beginSchoolNational.split("/")
                newCountry.set_action(datetime.date(int("20"+schoolNational[2]),
                                                int(schoolNational[0]),
                                                int(schoolNational[1])),
                                  "School_closure_national")
            if not countryInfo[i]["Curfew"] == "":
                beginCurfew             = countryInfo[i]["Curfew"]
                dateCurfew              = beginCurfew.split("/")
                newCountry.Curfew = datetime.date(int("20"+dateCurfew[2]),
                                                  int(dateCurfew[0]),
                                                  int(dateCurfew[1]))
            if not countryInfo[i]["Total number of tests"] == "":
                newCountry.TotalNumberOfTests = \
                    int(countryInfo[i]["Total number of tests"])
            if not countryInfo[i]["Corona tests /1000000 people"] == "":
                newCountry.CoronaTestsPerCitizen = \
                    int(countryInfo[i]["Corona tests /1000000 people"])
        
        if key in countriesAdd:
            i = countriesAdd.index(key)
            if not additionalInfo[i]["Population (2017)"] == "":
                newCountry.PopulationTotal = \
                    int(additionalInfo[i]["Population (2017)"])
            if not additionalInfo[i]["Surface area /km2 (2017)"] == "":
                newCountry.Area = int(additionalInfo[i]["Surface area /km2 (2017)"])
            if not additionalInfo[i]["Population density /km2"] == "":
                newCountry.PopulationDensity = \
                    float(additionalInfo[i]["Population density /km2"])
            if not additionalInfo[i]["GDP per capita /US$ (2017)"] == "":
                newCountry.GDPPerCapita = \
                    int(additionalInfo[i]["GDP per capita /US$ (2017)"])
            if not additionalInfo[i]["Physicians /1000 people (2015)"] == "":
                newCountry.PhysicianDensity = \
                    float(additionalInfo[i]["Physicians /1000 people (2015)"])
            if not additionalInfo[i]["Health expenditure per capita /US$ (2016)"] == "":
                newCountry.HealthExpenditureperCapita = \
                    float(additionalInfo[i]["Health expenditure per capita /US$ (2016)"])
            if not additionalInfo[i]["Hospital beds /1000 people (2019?)"] == "":
                newCountry.HospitalBedsDensity = \
                    float(additionalInfo[i]["Hospital beds /1000 people (2019?)"])
        countryList.append(newCountry)
    return countryList


def parseRegionDataGermany():
    """
    Read Statistical Data about regions in Germany.

    Returns
    -------
    List of Region Objects with Information.

    """
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
    return regionList