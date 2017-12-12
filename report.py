#!env/bin/python
import argparse
import datetime
from collections import Counter

from peewee import fn

from  ckuhl.models import PageView


# Take in command line arguments
parser = argparse.ArgumentParser(description='Run reports on ckuhl.com')
parser.add_argument('action',
        help='''The action to take:
        One of:
        TODO
        ''')
args = parser.parse_args()

# TODO: Modularize into last n days
week_ago = datetime.date.today() - datetime.timedelta(days=7)
base = PageView.select().where(PageView.timestamp >= week_ago)

# define various actions to take
def page_views():
    """Total number of page views"""
    print(base.count())

def unique_ips():
    """Total number of unique IP addresses"""
    print(base.select(PageView.ip).group_by(PageView.ip).count())

def top_n_pages(n=10):
    print(base.select(PageView.title, fn.Count(PageView.id))
            .group_by(PageView.title)
            .order_by(fn.Count(PageView.id).desc())
            .tuples())[:n]

def top_n_useragents(n=5):
    c = Counter(pv.headers.get('User-Agent') for pv in base)
    print(c.most_common(n))

def get_browsing_sessions(n=10):
    inner = base.select(PageView.ip, PageView.url).order_by(PageView.timestamp)
    query = (PageView.select(PageView.ip, fn.GROUP_CONCAT(PageView.url).alias('urls'))
        .from_(inner.alias('t1'))
        .group_by(PageView.ip)
        .order_by(fn.Count(PageView.url).desc()))
    print({pv.ip: pv.urls.split(',') for pv in query[:n]})

# Create a mapping of command line - functions
actions = {
    'hits': page_views,
    'ips': unique_ips,
    'top10': top_n_pages,
    'uas': top_n_useragents,
    'sessions': get_browsing_sessions,
}


# Run the desired function
try:
    actions[args.action]()
except KeyError:
    print('ERROR: `%s` is not a known report' % args.action)

