#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# jre - Japan Real Estate Transaction Prices Downloader
# https://github.com/helloryosuke/japan-real-estate-data
#
# Copyright 2021-2022 Ryosuke Inaba
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from .common import Date

class TradeList:
    """Class to construct TradeList request parameter for Request class
    """

    def __init__(self, start_date: Date, end_date: Date,
                area: str = "", city: str = "", station: str = ""):
        """Initialize TradeList object

        Args:
            start_date (Date): Starting date of date range to get data for
            end_date (Date): Ending date of date range to get data for
            area (str, optional): Area of data. Defaults to "".
            city (str, optional): City of data. Defaults to "".
            station (str, optional): Location of city. Defaults to "".

            Specify one of area, city, or station. If multiple are specified,
            one of the 3 will be used in the order of area, city, and station.
        """

        self._validate_params(area, city, station) # pre-validation of parameters

        self._start_date: Date = start_date
        self._end_date: Date = end_date 
        self._path: str = "/TradeListSearch" # data path for api

        # store list of specified location parameters (age, city, or station)
        # location getter will determine which parameter to apply
        self._params = [
            {
                "key": "area",
                "value": area
            },
            {
                "key": "city",
                "value": city
            },
            {
                "key": "station",
                "value": station
            }
        ]

    @property
    def start_date(self) -> str:
        """str: start date in YYYYQ format (year + quarter)
        """
        return f"{self._start_date.year}{self._start_date.quarter}"

    @property
    def end_date(self) -> str:
        """str: end date in YYYYQ format (year + quarter)
        """
        return f"{self._end_date.year}{self._end_date.quarter}"

    @property
    def location(self) -> str:
        """str: specified location to get data for
        """
        return list(filter(lambda item: len(item["value"]) > 0, self._params))[0]

    @property
    def query(self):
        """finalized query string to append to request
        """
        return f"{self._path}?from={self.start_date}&to={self.end_date}&{self.location['key']}={self.location['value']}"

    def _validate_params(self, area: str, city: str, station: str):
        """Validate the parameters used to specify either area, city, or station

        Args:
            area (str): Area of data
            city (str): City of data
            station (str): Station of data
        """

        # if case one of area, city, or station is not specified as string, throw error
        if not(isinstance(area, str) and isinstance(city, str) and isinstance(station, str)):
            raise ValueError("Area, city, and station must be specified in string")

        # if none of area, city, or station are specified, throw error
        if area + city + station == "":
            raise ValueError("Must specify either area, city, or station")
    
class CityList:
    """Class to construct CityList request parameter for Request class
    """

    def __init__(self, area: int):
        """Initialize the CityList object

        Args:
            area (int): area to get the city list for
        """

        self._validate_area(area) # pre-validate the area parameter

        self._area: int = area
        self._path: str = "/CitySearch" # data path for api

    @property
    def area(self) -> int:
        """int: Specified area to search for
        """
        return self._area

    @property
    def query(self) -> str:
        """finalized query string to append to request
        """
        return f"{self._path}?area={self._area}"

    def _validate_area(self, area: int) -> None:
        """Validates the area value

        Args:
            area (str): area to get the city list for
        """
        
        if not isinstance(area, int):
            raise ValueError("Specify an integer for area")