from typing import Dict
import requests


class HttpRequester:
    def __init__(self) -> None:
        self.__url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm'
        self.__header = {
            'User-agent': 'Mozilla/5.0'
        }

    def request_from_page(self) -> Dict[int, str]:
        response = requests.get(self.__url, headers=self.__header, timeout=5)
        return {
            "status_code": response.status_code,
            "html": response.text
        }
