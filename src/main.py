#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 17:20:10 2020

@author: 
"""
import sys
sys.path.append(r"../lib")
import utils

regionList = utils.parseRegionDataGermany()
regionList[2].printInfo()

countryList = utils.parseCountryData()
countryList[2].printInfo()

#TODO: Process Data
