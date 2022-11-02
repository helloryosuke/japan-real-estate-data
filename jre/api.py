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

import pandas as _pd
import json as _json
import requests as _requests
from .data import TradeList
from .data import CityList

class Response:
    """Class to format and store response
    """

    def __init__(self, data: dict):
        """Initialize the Response object

        Args:
            data (dict): data consisting of response status and values
        """
        self._status = data["status"] # response status
        
        # if response status is ERROR, set value of data to None
        if self._status == "ERROR": self._value = None
        else: self._value = data["data"] # otherwise, set data

    @property
    def status(self) -> str:
        """str: status of the response. 
        Value will be "OK" if successfully retrieved, "ERROR" if not.
        """
        return self._status

    def json(self) -> dict:
        """Get data in dict/json format
        """
        return self._value

    def df(self) -> _pd.DataFrame:
        """Get data in Pandas DataFrame format
        """
        return _pd.DataFrame(self._value)

class Request:
    """Class to construct the request for the specified data field and execute request.
    """

    def __init__(self, data: TradeList|CityList, lang: str = "jpn"):
        """Initialize the Requests object

        Args:
            data (TradeList | CityList): specify data field to retrieve
            lang (str, optional): Specify "jpn" for Japanese data. All other values will produce English data. Defaults to "jpn".
        """

        lang_path = "webland" if lang.lower() == "jpn" else "webland_english" # determine path of request depending on language specified
        self._url: str = f"https://www.land.mlit.go.jp/{lang_path}/api" + data.query # construct full url

    def execute(self, timeout: int = 20) -> Response:
        """Executes the request

        Args:
            timeout (int, optional): timeout of request in seconds. Defaults to 20.

        Returns:
            Response: response of request execution
        """

        response = _requests.get(self._url, timeout=timeout) # send request
        return Response(_json.loads(response.text)) # transform response to Response object