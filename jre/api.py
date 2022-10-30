import pandas as pd
import json
import requests
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

    def df(self) -> pd.DataFrame:
        """Get data in Pandas DataFrame format
        """
        return pd.DataFrame(self._value)

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

        response = requests.get(self._url, timeout=timeout) # send request
        return Response(json.loads(response.text)) # transform response to Response object