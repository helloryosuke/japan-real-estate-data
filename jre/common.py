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

from datetime import date as _date

class Date(_date):
    """Class to store date information

    Attributes:
        year (int): Year of date
        month (int): Month of date
        day (int): Day of date
    """

    def __init__(self, year: int, month: int, day: int):
        """Initialize Date object

        Args:
            year (int): Year of date
            month (int): Month of date
            day (int): Day of date
        """
        super().__init__()

    @property
    def quarter(self):
        """int: Quarter of date
        """
        return self.month // 4 + 1