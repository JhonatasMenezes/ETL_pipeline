# pylint: disable=line-too-long
import datetime
from src.stages.contracts.transform_contract import TransformContract

transform_contract_mock = TransformContract(
    load_content=[
        {'first_name': 'Igor', 'second_name': 'Zakowortny', 'surname': None, 'artist_id': '20099', 'link': 'https://web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=20099', 'extraction_date': datetime.date(2024, 4, 4)},
        {'first_name': 'Alfredo', 'second_name': 'Zalce', 'surname': None, 'artist_id': '11597', 'link': 'https://web.archive.org/web/20121007172955/https:/www.nga.gov/cgi-bin/tsearch?artistid=11597', 'extraction_date': datetime.date(2024, 4, 4)},
        {'first_name': 'Giampietro', 'second_name': 'Zanotti', 'surname': None, 'artist_id': '11631', 'link': 'https://web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=11631', 'extraction_date': datetime.date(2024, 4, 4)},
        {'first_name': 'Wou-Ki', 'second_name': 'Zao', 'surname': None, 'artist_id': '3427', 'link': 'https://web.archive.org/web/20121007172955/https://www.nga.gov/cgi-bin/tsearch?artistid=3427', 'extraction_date': datetime.date(2024, 4, 4)}
    ]
)
