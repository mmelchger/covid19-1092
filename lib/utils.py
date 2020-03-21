 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 01:00:42 2020

@author: enno
"""
import datetime
import os
import csv

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
        Set Maßname in Region.

        Parameters
        ----------
        aBegin : TYPE
            DESCRIPTION.
        aName : string
            Name to identify
        aEnd : TYPE, optional
            same type as Begin

        Returns
        -------
        None.

        """
        #TODO: find Type of aBegin, update Docstring
        Massname = namedtuple("Massname", ["Begin", "End", "Name"])
        self.Action.append(Massname(aBegin, aEnd, aName))
    
    
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

def parseRegionData():
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