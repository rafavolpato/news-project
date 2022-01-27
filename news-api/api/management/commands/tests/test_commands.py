import os
import pickle
from unittest.mock import patch, MagicMock

import pytest as pytest
from api.management.commands import fetch_feed
from api.models import Entry
from news_project.utils import convert_feed_date

pytestmark = pytest.mark.django_db


@pytest.fixture
def entries() -> Entry:
    """
    From entries.txt returns entries parsed
    """
    file_name = os.path.join(os.path.dirname(__file__), 'entries.txt')
    with open(file_name, "rb") as f:
        entries = pickle.load(f)
    return entries


def test_parse_entries(entries) -> None:
    """
    receive entries that came from entries.txt.
    call parse_entries and check if they match
    """
    parsed_feeds = fetch_feed.parse_entries(entries)
    assert len(parsed_feeds) == len(entries)
    for i in range(len(parsed_feeds)):
        assert parsed_feeds[i]["id"] == entries[i]["id"]
        assert parsed_feeds[i]["title"] == entries[i]["title"]
        assert parsed_feeds[i]["link"] == entries[i]["link"]
        assert parsed_feeds[i]["published"] == convert_feed_date(entries[i]["published"])
        assert parsed_feeds[i]["summary"] == entries[i]["summary"]


def test_insert_entries(entries) -> None:
    """
    receive entries that came from entries.txt.
    call parse_entries and and the call insert_entries
    check if all the feeds were inserted into the datebase
    """
    parsed_feeds = fetch_feed.parse_entries(entries)
    site = {"name": "mashable", "url": "https://it.mashable.com/feed.xml"}
    feeds_inserted = fetch_feed.insert_entry(site, parsed_feeds)
    assert feeds_inserted == 40
    assert_entries(site, parsed_feeds)


def test_handle_command(entries) -> None:
    """
    receive entries that came from entries.txt.
    call parse_entries and and the call insert_entries
    mock get_entries method before calling handle to make sure that it is going to get data from entries
    check if all the feeds were inserted into the datebase
    """
    parsed_feeds = fetch_feed.parse_entries(entries)
    with patch('api.management.commands.fetch_feed.get_entries') as mock:
        mock.return_value = parsed_feeds
        command = fetch_feed.Command()
        command.handle()
    site = {"name": "mashable", "url": "https://it.mashable.com/feed.xml"}
    assert_entries(site, parsed_feeds)


def assert_entries(site, parsed_feeds) -> Entry:
    """
    check if the parsed_feed from an specific site was inserted into the database
    """
    for feed in parsed_feeds:
        entry = Entry.objects.filter(site_name=site["name"],
                                     title=feed["title"],
                                     link=feed["link"],
                                     published=feed["published"],
                                     summary=feed["summary"],
                                     click_count=0
                                     ).count()
        assert entry > 0
