from typing import List, Dict

class HtmlCollectorSpy:

    def __init__(self) -> None:
        self.collect_essential_information_atributes = {}

    def collect_essential_information(self, html: str) -> List[Dict[str, str]]:
        self.collect_essential_information_atributes['html'] = html
        return [{"name": 'someName', "link": 'https://something.com'}]
