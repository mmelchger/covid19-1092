 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 01:00:42 2020

@author: enno
"""

class region():
    """
    Region object.
    """

    def __init__(self, id):
        """
        Create Region object.

        Parameters
        ----------
        id : named Tuple
            id as used in JHU-Covid19 Dataset:
                ("Province/State", "Country/Region", "Lat", "Long")
        name : String
            Name of Region
            i.e. "Landkreis Osnabrück"
        
        Returns
        -------
        None.

        """
        self.Province   = id("Province")
        self.Country    = id("Country")
        self.Lat        = id("Lat")
        self.Long       = id("Long")
        self.id         = id
        
        # Empty Init
        self.Bevoelkerungsdichte = None
        self.Zeitreihe           = None
        self.Massnahme           = []


    def get_id(self):
        """Get namedTuple with id information."""
        return self.id


    def get_name(self):
        """Get Name of Province."""
        if self.Province is None:
            raise UserWarning("No data set for Name/Province")
        return self.Province


    def get_infection(self, aDatetime):
        """
        Get Number of infected Persons at date aDatetime

        Parameters
        ----------
        datetime : TYPE
            DESCRIPTION.

        returns
        -------
        int Number of Infected Persons

        """
        raise NotImplementedError("get_infection is not yet implemented")
        #TODO: implement


    def set_zeitreihe(self, aDataset):
        """
        Set Zeitreihen Data for Region

        Parameters
        ----------
        aDataset : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        raise NotImplementedError("set_zeitreihe is not yet implemented")
        #TODO: implement


    def set_massname(self, aBegin, aName, aEnd=None):
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
        self.Massnahme.append(Massname(aBegin, aEnd, aName))

