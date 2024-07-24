from http import HTTPStatus

import pytest
import requests

from .fav_model import ErrorModel

urlPath = "https://regions-test.2gis.com/v1/favorites"


@pytest.fixture(autouse=True)
def get_token(request):
    response = requests.post("https://regions-test.2gis.com/v1/auth/tokens")
    cookies = response.cookies.get_dict()
    request.cls.token = cookies["token"]


class TestObligatory:

    def test_create_fav_no_token(self):
        payload = {"title": "Ottawa",
                   "lon": -75.695145,
                   "lat": 45.423605
                   }

        session = requests.Session()

        response = session.post(
            urlPath,
            data=payload,
        )

        json_response: ErrorModel = response.json()

        assert (response.status_code == HTTPStatus.UNAUTHORIZED)
        assert ("Параметр 'token' является обязательным" ==
                json_response['error']['message'])

    def test_create_fav_no_title(self):
        payload = {"lon": -75.695145,
                   "lat": 45.423605,
                   }

        session = requests.Session()

        response = session.post(
            urlPath,
            data=payload,
            cookies={"token": self.token}
        )

        json_response: ErrorModel = response.json()

        assert (response.status_code == HTTPStatus.BAD_REQUEST)
        assert ("Параметр 'title' является обязательным" ==
                json_response['error']['message'])

    def test_create_fav_no_lon(self):
        payload = {"title": "Ottawa",
                   "lat": 45.423605,
                   }

        session = requests.Session()

        response = session.post(
            urlPath,
            data=payload,
            cookies={"token": self.token}
        )

        json_response: ErrorModel = response.json()

        assert (response.status_code == HTTPStatus.BAD_REQUEST)
        assert ("Параметр 'lon' является обязательным" ==
                json_response['error']['message'])

    def test_create_fav_no_lat(self):
        payload = {"title": "Ottawa",
                   "lon": -75.695145,
                   }

        session = requests.Session()

        response = session.post(
            urlPath,
            data=payload,
            cookies={"token": self.token}
        )

        json_response: ErrorModel = response.json()

        assert (response.status_code == HTTPStatus.BAD_REQUEST)
        assert ("Параметр 'lat' является обязательным" ==
                json_response['error']['message'])

    def test_fault_method_get(self):
        payload = {"title": "Ottawa",
                   "lon": -75.695145,
                   "lat": 45.423605
                   }

        session = requests.Session()

        response = session.get(
            urlPath,
            data=payload,
            cookies={"token": self.token}
        )

        assert (response.status_code == HTTPStatus.METHOD_NOT_ALLOWED)

    def test_fault_method_put(self):
        payload = {"title": "Ottawa",
                   "lon": -75.695145,
                   "lat": 45.423605
                   }

        session = requests.Session()

        response = session.put(
            urlPath,
            data=payload,
            cookies={"token": self.token}
        )

        assert (response.status_code == HTTPStatus.METHOD_NOT_ALLOWED)

    def test_fault_method_delete(self):
        payload = {"title": "Ottawa",
                   "lon": -75.695145,
                   "lat": 45.423605
                   }

        session = requests.Session()

        response = session.delete(
            urlPath,
            data=payload,
            cookies={"token": self.token}
        )

        assert (response.status_code == HTTPStatus.METHOD_NOT_ALLOWED)