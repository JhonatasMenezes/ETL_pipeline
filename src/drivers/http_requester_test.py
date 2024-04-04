from .http_requester import HttpRequester

def test_request_from_page(requests_mock):
    url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm'
    reponse_context = "<h1>Ola, Mundo!</h1>"
    requests_mock.get(url, status_code=200, text=reponse_context)

    http_requester = HttpRequester()
    request_response = http_requester.request_from_page()

    assert 'status_code' in request_response
    assert 'html' in request_response
    assert request_response["status_code"] == 200
    assert request_response["html"] == reponse_context
