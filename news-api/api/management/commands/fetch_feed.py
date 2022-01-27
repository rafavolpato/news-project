import datetime
import pickle

from django.core.management.base import BaseCommand

import news_project.utils
from api.models import Entry
from news_project import utils
import feedparser

class Command(BaseCommand):
    """
    Get rss feeds from 3 sites:
        https://it.mashable.com/feed.xml
        https://techcrunch.com/feed/
        https://www.theverge.com/rss/index.xml
    And store them in the datebase
    """

    def __init__(self, stdout=None, stderr=None, no_color=False, force_color=False):
        """
        Initialize counters
        """
        super().__init__(stdout, stderr, no_color, force_color)
        self.total_records_read = 0
        self.total_records_added = 0

    def handle(self, *args, **options):
        """"
        Perform reading feeds from feeds urls and insert into the database
        """
        self.stdout.write("Loading news-site...", ending='\n')

        sites = [
            {"name": "mashable", "url": "https://it.mashable.com/feed.xml"},
            {"name": "techrunch", "url": "https://techcrunch.com/feed/"},
            {"name": "theverge", "url": "https://www.theverge.com/rss/index.xml"}
        ]

        for site in sites:
            self.stdout.write(f"Reading feeds from {site['name']}", ending='\n')
            entries = get_entries(site)  # return feed data as a list
            self.stdout.write(f"Total records read from {site['name']}: {len(entries)}", ending='\n')
            self.stdout.write(f"Adding feeds...", ending='\n')
            total_added_entries = insert_entry(site, entries)
            self.stdout.write(f"Total records added from {site['name']}: {total_added_entries}", ending='\n')
            self.total_records_read += len(entries)
            self.total_records_added += total_added_entries

        self.stdout.write(f"Total records read: {self.total_records_added}", ending='\n')
        self.stdout.write(f"Total records added: {self.total_records_added}", ending='\n')


def get_entries(site=None):
    """
    From site, parse rss
    """
    # parsing blog feed
    feed = feedparser.parse(site["url"])

    # getting lists of entries via .entries
    entries = feed.entries
    # import os
    # file_name = os.path.join(os.path.dirname(__file__), 'tests/entries.txt')
    # outfile = open(file_name, 'wb')
    # pickle.dump(entries, outfile)
    # outfile.close()

    entry_list = parse_entries(entries)

    return entry_list  # returning the details which is dictionary


def parse_entries(entries):
    """
    Serialize entries from feed_parser to a dictionary
    """
    entry_list = []
    for entry in entries:
        temp = dict()

        # if any entry doesn't have information then throw error.
        try:
            temp["id"] = entry["id"]
            temp["title"] = entry["title"]
            temp["link"] = entry["link"]
            temp["published"] = utils.convert_feed_date(entry["published"])
            temp["summary"] = entry["summary"]
            entry_list.append(temp)
        except:
            pass

    return entry_list


def insert_entry(site, entries):
    """
    From a dict insert into the database
    """
    actual_feed_count = 0
    for entry in entries:
        entry_rec = Entry.objects.filter(site_name=site["name"], link=entry["link"])
        if not entry_rec:
            Entry.objects.create(
                site_name=site["name"],
                link=entry["link"],
                title=entry["title"],
                summary=entry["summary"],
                published=entry["published"],
                click_count=0
            )
            actual_feed_count += 1
    return actual_feed_count
