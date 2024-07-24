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


class TestFavs:

    def test_create_fav_empty_title(self):
        payload = {"title": "",
                   "lon": -75.695145,
                   "lat": 45.423605
                   }

        session = requests.Session()

        response = session.post(
            urlPath,
            data=payload,
            cookies={"token": self.token}
        )

        json_response: ErrorModel = response.json()

        assert (response.status_code == HTTPStatus.BAD_REQUEST)
        assert ("Параметр 'title' не может быть пустым" ==
                json_response['error']['message'])

    def test_create_fav_integer_title(self):
        payload = {"title": 2,
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

        json_response: ErrorModel = response.json()

        assert (response.status_code == HTTPStatus.BAD_REQUEST)
        assert ("Параметр 'title' должен содержать не более 999 символов" ==
                json_response['error']['message'])

    def test_create_fav_bool_title(self):
        payload = {"title": False,
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

        json_response: ErrorModel = response.json()

        assert (response.status_code == HTTPStatus.BAD_REQUEST)
        assert ("Параметр 'title' должен содержать не более 999 символов" ==
                json_response['error']['message'])

    def test_create_fav_number_title(self):
        payload = {"title": "2",
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

    def test_create_fav_symbols_title(self):
        payload = {"title": "?",
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

    def test_create_fav_title999(self):
        title999 = "a" * 999
        payload = {"title": title999,
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

    def test_create_fav_title1000(self):
        title1000 = "a" * 1000
        payload = {"title": title1000,
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

        json_response: ErrorModel = response.json()

        assert (response.status_code == HTTPStatus.BAD_REQUEST)
        assert ("Параметр 'title' должен содержать не более 999 символов" ==
                json_response['error']['message'])

    def test_create_fav_title1001(self):
        title1001 = "a" * 1001
        payload = {"title": title1001,
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

        json_response: ErrorModel = response.json()

        assert (response.status_code == HTTPStatus.BAD_REQUEST)
        assert ("Параметр 'title' должен содержать не более 999 символов" ==
                json_response['error']['message'])

    def test_create_fav_cyrillic_title(self):
        payload = {"title": "Оттава",
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

    def test_create_fav_whitespace_title(self):
        payload = {"title": " ",
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

    def test_create_fav_mixed_title(self):
        payload = {"title": "Щu7^ ФйG",
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

    def test_create_fav_title_is_even_lon(self):
        payload = {"title": "-75.695145",
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
