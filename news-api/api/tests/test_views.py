import pytest as pytest
from django.urls import reverse

from api.models import Entry
from news_project.utils import convert_feed_date
from datetime import datetime, timezone

entry_list_url = reverse('entry-list')
entry_detail_url = reverse('entry-detail', args=[1])
pytestmark = pytest.mark.django_db


@pytest.fixture
def new_entry_record() -> Entry:
    """
    Add 1 record to the database
    """
    entry = Entry()
    entry.site_name = 'mashable'
    entry.click_count = 1
    entry.link = 'http://site1.com'
    entry.summary = 'summary'
    entry.published = convert_feed_date('Wed, 26 Jan 2022 10:00:28 +0000')
    entry.save()
    return entry


@pytest.fixture
def assert_entries(**kwargs) -> Entry:
    """
    Check if 2 entries are equal - except click_count (will be checked elsewhere)
    """
    def _assert_entries(**kwargs) -> None:
        entry_response = kwargs.pop('entry_response', None)
        entry_record = kwargs.pop('entry_record', None)

        assert entry_record.site_name == entry_response["site_name"]
        assert entry_record.link == entry_response["link"]
        assert entry_record.summary == entry_response["summary"]
        assert datetime.strftime(entry_record.published, '%Y-%m-%dT%H:%M:%SZ') == entry_response["published"]


    return _assert_entries


def test_api_entry_list_error_400(client) -> None:
    """
    Check if it returns status code 400 since the site was not infromed to the GET method
    """
    response = client.get(entry_list_url)
    assert response.status_code == 400


def test_api_entry_list_succeed(client, new_entry_record, assert_entries) -> None:
    """
    Check if brand new record is retrieved by using GET method
    """
    entry = new_entry_record
    response = client.get(entry_list_url, {'site': entry.site_name, 'id': entry.pk })
    assert response.status_code == 200
    result = response.data['results'][0]
    assert_entries(**{'entry_record': entry, 'entry_response': result})
    assert entry.click_count == result['click_count']


def test_api_entry_patch_detail_error_404(client) -> None:
    """
    Check if a record that doesn`t exist will return 404
    """
    entry = Entry.objects.filter(pk=1)
    if entry:
        entry.delete()
    response = client.patch(entry_detail_url)

    assert response.status_code == 404


def test_api_entry_patch_detail(client, new_entry_record, assert_entries) -> None:
    """
    Check if a new inserted record is retrieved and it updates click_count correctly
    """
    entry = new_entry_record
    response = client.patch(entry_detail_url)
    assert response.status_code == 200
    assert_entries(**{'entry_record': entry, 'entry_response': response.data})
    assert response.data["click_count"] == 2
