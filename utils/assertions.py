from favs_testing.models.fav_place import Favorite

def assert_fav(
        expected_fav: Favorite,
        actual_fav: dict
):
    assert (expected_fav['title'] == actual_fav['title'])

    assert (expected_fav['lon'] == actual_fav['lon'])

    assert (expected_fav['lon'] == actual_fav['lon'])

    if 'color' in actual_fav:
        assert (expected_fav['color'] == actual_fav['color'])
