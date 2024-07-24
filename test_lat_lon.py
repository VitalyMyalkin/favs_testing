from http import HTTPStatus

import pytest
import requests

from .fav_model import Favorite, ErrorModel
from .assertions import assert_fav

urlPath = "https://regions-test.2gis.com/v1/favorites"


@pytest.fixture(autouse=True)
def get_token(request):
    response = requests.post("https://regions-test.2gis.com/v1/auth/tokens")
    cookies = response.cookies.get_dict()
    request.cls.token = cookies["token"]


class TestLatLon:

    def test_create_fav_00(self):
        payload = {"title": "00",
                   "lon": 0,
                   "lat": 0,
                   "color": "YELLOW"
                   }

        session = requests.Session()

        response = session.post(
            urlPath,
            data=payload,
            cookies={"token": self.token}
        )

        json_response: Favorite = response.json()

        assert (response.status_code == HTTPStatus.OK)
        assert_fav(
            expected_fav=json_response,
            actual_fav=payload
        )

    def test_create_fav_negative(self):
        payload = {"title": "-1",
                   "lon": -1,
                   "lat": -1,
                   "color": "YELLOW"
                   }

        session = requests.Session()

        response = session.post(
            urlPath,
            data=payload,
            cookies={"token": self.token}
        )

        json_response: Favorite = response.json()

        assert (response.status_code == HTTPStatus.OK)
        assert_fav(
            expected_fav=json_response,
            actual_fav=payload
        )

    def test_create_fav_max_lon(self):
        payload = {"title": "lon500",
                   "lon": 500,
                   "lat": 45.423605,
                   "color": "GREEN"
                   }

        session = requests.Session()

        response = session.post(
            urlPath,
            data=payload,
            cookies={"token": self.token}
        )

        json_response: ErrorModel = response.json()

        assert (response.status_code == HTTPStatus.BAD_REQUEST)
        assert ("Параметр 'lon' должен быть не более 180" ==
                json_response['error']['message'])

    def test_create_fav_min_lon(self):
        payload = {"title": "lon-500",
                   "lon": -500,
                   "lat": 45.423605,
                   "color": "GREEN"
                   }

        session = requests.Session()

        response = session.post(
            urlPath,
            data=payload,
            cookies={"token": self.token}
        )

        json_response: ErrorModel = response.json()

        assert (response.status_code == HTTPStatus.BAD_REQUEST)
        assert ("Параметр 'lon' должен быть не менее -180" ==
                json_response['error']['message'])

    def test_create_fav_string_lon(self):
        payload = {"title": "Here",
                   "lon": "Here",
                   "lat": -1,
                   "color": "YELLOW"
                   }

        session = requests.Session()

        response = session.post(
            urlPath,
            data=payload,
            cookies={"token": self.token}
        )

        json_response: ErrorModel = response.json()

        assert (response.status_code == HTTPStatus.BAD_REQUEST)
        assert ("Параметр 'lon' должен быть числом" ==
                json_response['error']['message'])

    def test_create_fav_symbol_lon(self):
        payload = {"title": "-1",
                   "lon": "/",
                   "lat": -1,
                   "color": "YELLOW"
                   }

        session = requests.Session()

        response = session.post(
            urlPath,
            data=payload,
            cookies={"token": self.token}
        )

        json_response: ErrorModel = response.json()

        assert (response.status_code == HTTPStatus.BAD_REQUEST)
        assert ("Параметр 'lon' должен быть числом" ==
                json_response['error']['message'])

    def test_create_fav_max_lat(self):
        payload = {"title": "lat500",
                   "lon": 45.423605,
                   "lat": 500,
                   "color": "GREEN"
                   }

        session = requests.Session()

        response = session.post(
            urlPath,
            data=payload,
            cookies={"token": self.token}
        )

        json_response: ErrorModel = response.json()

        assert (response.status_code == HTTPStatus.BAD_REQUEST)
        assert ("Параметр 'lat' должен быть не более 90" ==
                json_response['error']['message'])

    def test_create_fav_min_lat(self):
        payload = {"title": "lat-500",
                   "lon": 45.423605,
                   "lat": -500,
                   "color": "GREEN"
                   }

        session = requests.Session()

        response = session.post(
            urlPath,
            data=payload,
            cookies={"token": self.token}
        )

        json_response: ErrorModel = response.json()

        assert (response.status_code == HTTPStatus.BAD_REQUEST)
        assert ("Параметр 'lat' должен быть не менее -90" ==
                json_response['error']['message'])

    def test_create_fav_string_lat(self):
        payload = {"title": "Here",
                   "lon": -1,
                   "lat": "Here",
                   "color": "YELLOW"
                   }

        session = requests.Session()

        response = session.post(
            urlPath,
            data=payload,
            cookies={"token": self.token}
        )

        json_response: ErrorModel = response.json()

        assert (response.status_code == HTTPStatus.BAD_REQUEST)
        assert ("Параметр 'lat' должен быть числом" ==
                json_response['error']['message'])

    def test_create_fav_symbol_lat(self):
        payload = {"title": "-1",
                   "lon": -1,
                   "lat": "/",
                   "color": "YELLOW"
                   }

        session = requests.Session()

        response = session.post(
            urlPath,
            data=payload,
            cookies={"token": self.token}
        )

        json_response: ErrorModel = response.json()

        assert (response.status_code == HTTPStatus.BAD_REQUEST)
        assert ("Параметр 'lat' должен быть числом" ==
                json_response['error']['message'])