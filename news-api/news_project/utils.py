from datetime import datetime, timezone
import re

MONTHS = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7,
         'Ago': 8, 'sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}

def convert_feed_date(date):
    """
    Receive a data that can be in two formats?
    format_starts_with_year = Wed, 26 Jan 2022 10:00:28 +0000
    format2 = 2022-01-27T09:55:36-05:00

    returns one datetime obj
    """
    format_starts_with_year = False
    if re.match(r"\d{4}", date) is not None:
        format_starts_with_year = True
        pattern = \
            re.compile(r'(?P<year>\d{4})'
                       r'-'
                       r'(?P<month>\d{2})'
                       r'-'
                       r'(?P<day>\d{2})'
                       r'T'
                       r'(?P<hour>\d{2})'
                       r':'
                       r'(?P<minute>\d{2})'
                       r':'
                       r'(?P<second>\d{2})'
                       r'-'
                       r'\d{2}'
                       r':'
                       r'\d{2}')
    else:
        pattern = \
            re.compile(r'^\w{3},\s'
                       r'(?P<day>\d{2})'
                       r'\s'
                       r'(?P<month>Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)'
                       r'\s'
                       r'(?P<year>\d{4})'
                       r'\s'
                       r'(?P<hour>\d{2})'
                       r':'
                       r'(?P<minute>\d{2})'
                       r':'
                       r'(?P<second>\d{2})'
                       r'\s\+\d{4}$')

    #Get a dic from matched string/groups
    res = pattern.search(date).groupdict()

    #when the format returns months like (jan, fev, mar, etc), tranlate it into a numver in MONTHS
    if not format_starts_with_year:
        res['month'] = int(MONTHS[res['month']])

    #convert values from str to int (from year, month, day, etc.)
    res = {key: int(value) for key, value in res.items()}

    date_time_obj = datetime(
        res['year'], res['month'], res['day'], res['hour'], res['minute'], res['second'], 0)

    #since the timezone in settings is True datetime must have timezone to insert in database
    date_time_obj = date_time_obj.replace(tzinfo=timezone.utc)

    return date_time_obj
