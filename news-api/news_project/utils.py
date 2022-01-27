from datetime import datetime, timezone
import re


def convert_feed_date(date):
    pattern = \
        re.compile(r'\w{3},\s(\d{2})\s(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s(\d{4})\s(\d{2}):(\d{2}):(\d{2})\s\+(\d{4})$')
    res = pattern.search(date).groups()[:]
    month = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7,
              'Ago': 8, 'sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
    day = int(res[0])
    month = int(month[res[1]])
    year = int(res[2])
    hour = int(res[3])
    minute = int(res[4])
    second = int(res[5])
    milisecond = int(res[6])
    date_time_obj = datetime(year, month, day, hour, minute, second, milisecond)
    date_time_obj = date_time_obj.replace(tzinfo=timezone.utc)
    return date_time_obj