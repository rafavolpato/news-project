from news_project.utils import convert_feed_date


def test_convert_feed_date():
    """
    Check if convert_feed_date is returning a valid/correct date
    """
    date = 'Wed, 26 Jan 2022 10:00:28 +0000'
    assert str(convert_feed_date(date)) == '2022-01-26 10:00:28+00:00'
    date = '2022-01-27T09:55:36-05:00'
    assert str(convert_feed_date(date)) == '2022-01-27 09:55:36+00:00'