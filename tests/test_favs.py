from http import HTTPStatus

import pytest
import requests

from favs_testing.models.fav_place import Favorite
from favs_testing.utils.assertions import assert_fav

urlPath = "https://regions-test.2gis.com/v1/favorites"


@pytest.fixture(autouse=True)
def get_token(request):
    response = requests.post("https://regions-test.2gis.com/v1/auth/tokens")
    cookies = response.cookies.get_dict()
    request.cls.token = cookies["token"]


class TestFavs:

    def test_create_fav(self):
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
