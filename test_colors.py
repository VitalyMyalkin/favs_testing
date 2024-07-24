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


class TestColors:

    def test_create_fav_no_color(self):
        payload = {"title": "Ottawa",
                   "lon": -75.695145,
                   "lat": 45.423605
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

    def test_create_fav_green(self):
        payload = {"title": "Ottawa",
                   "lon": -75.695145,
                   "lat": 45.423605,
                   "color": "GREEN"
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

    def test_create_fav_yellow(self):
        payload = {"title": "Ottawa",
                   "lon": -75.695145,
                   "lat": 45.423605,
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

    def test_create_fav_red(self):
        payload = {"title": "Ottawa",
                   "lon": -75.695145,
                   "lat": 45.423605,
                   "color": "RED"
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

    def test_create_fav_blue(self):
        payload = {"title": "Ottawa",
                   "lon": -75.695145,
                   "lat": 45.423605,
                   "color": "BLUE"
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

    def test_create_fav_black(self):
        payload = {"title": "Ottawa",
                   "lon": -75.695145,
                   "lat": 45.423605,
                   "color": "BLACK"
                   }

        session = requests.Session()

        response = session.post(
            urlPath,
            data=payload,
            cookies={"token": self.token}
        )

        json_response: ErrorModel = response.json()

        assert (response.status_code == HTTPStatus.BAD_REQUEST)
        assert ("Параметр 'color' может быть одним из следующих значений: BLUE, GREEN, RED, YELLOW" ==
                json_response['error']['message'])

    def test_create_fav_color_cyrillic(self):
        payload = {"title": "Оттава",
                   "lon": -75.695145,
                   "lat": 45.423605,
                   "color": "КРАСНЫЙ"
                   }

        session = requests.Session()

        response = session.post(
            urlPath,
            data=payload,
            cookies={"token": self.token}
        )

        json_response: ErrorModel = response.json()

        assert (response.status_code == HTTPStatus.BAD_REQUEST)
        assert ("Параметр 'color' может быть одним из следующих значений: BLUE, GREEN, RED, YELLOW" ==
                json_response['error']['message'])

    def test_create_fav_color_symbols(self):
        payload = {"title": "Оттава",
                   "lon": -75.695145,
                   "lat": 45.423605,
                   "color": "/"
                   }

        session = requests.Session()

        response = session.post(
            urlPath,
            data=payload,
            cookies={"token": self.token}
        )

        json_response: ErrorModel = response.json()

        assert (response.status_code == HTTPStatus.BAD_REQUEST)
        assert ("Параметр 'color' может быть одним из следующих значений: BLUE, GREEN, RED, YELLOW" ==
                json_response['error']['message'])

    def test_create_fav_color_numbers(self):
        payload = {"title": "Оттава",
                   "lon": -75.695145,
                   "lat": 45.423605,
                   "color": "8"
                   }

        session = requests.Session()

        response = session.post(
            urlPath,
            data=payload,
            cookies={"token": self.token}
        )

        json_response: ErrorModel = response.json()

        assert (response.status_code == HTTPStatus.BAD_REQUEST)
        assert ("Параметр 'color' может быть одним из следующих значений: BLUE, GREEN, RED, YELLOW" ==
                json_response['error']['message'])

    def test_create_fav_color_empty(self):
        payload = {"title": "Оттава",
                   "lon": -75.695145,
                   "lat": 45.423605,
                   "color": ""
                   }

        session = requests.Session()

        response = session.post(
            urlPath,
            data=payload,
            cookies={"token": self.token}
        )

        json_response: ErrorModel = response.json()

        assert (response.status_code == HTTPStatus.BAD_REQUEST)
        assert ("Параметр 'color' может быть одним из следующих значений: BLUE, GREEN, RED, YELLOW" ==
                json_response['error']['message'])