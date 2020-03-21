 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 01:00:42 2020

@author: enno
"""
import datetime

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

        self.PopulationDensity = None
        self.PopulationTotal   = None
        self.PopulationMale    = None
        self.PopulationFemale  = None
        self.RegionIDZensus    = None
        self.TimeSeries        = None
        self.Action            = None


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

